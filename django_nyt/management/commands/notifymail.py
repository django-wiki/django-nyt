from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
import os
import sys
import time
import smtplib
import logging
from datetime import datetime
from optparse import make_option

from django.contrib.sites.models import Site
from django.core import mail
from django.core.management.base import BaseCommand
from django.template.loader import render_to_string
from django.utils.translation import ugettext as _, activate, deactivate
from django.conf import settings

from django_nyt import models
from django_nyt import settings as nyt_settings


# Daemon / mail loop sleep between each database poll (seconds)
SLEEP_TIME = 120


class Command(BaseCommand):
    can_import_settings = True
    # @ReservedAssignment
    help = 'Sends notification emails to subscribed users taking into account the subscription interval'
    option_list = getattr(BaseCommand, 'option_list', ()) + (
        make_option('--daemon', '-d',
                    action='store_true',
                    dest='daemon',
                    help='Go to daemon mode and exit'),
        make_option('--cron', '-c',
                    action='store_true',
                    dest='cron',
                    help='Do not loop, just send out emails once and exit'),
        make_option('--pid-file', '',
                    action='store',
                    dest='pid',
                    help='Where to write PID before exiting',
                    default='/tmp/nyt_daemon.pid'),
        make_option('--log-file', '',
                    action='store',
                    dest='log',
                    help='Where daemon should write its log',
                    default="/tmp/nyt_daemon.log"),
        make_option('--no-sys-exit', '',
                    action='store_true',
                    dest='no_sys_exit',
                    help='Skip sys-exit after forking daemon (for testing purposes)'),
        make_option('--daemon-sleep-interval', '',
                    action='store',
                    dest='sleep_time',
                    help='Minimum sleep between each polling of the database.',
                    default=SLEEP_TIME),
    )

    def _send_user_notifications(self, context, connection):
        subject = _(nyt_settings.EMAIL_SUBJECT)

        message = render_to_string(
            'emails/notification_email_message.txt',
            context
        )
        email = mail.EmailMessage(
            subject, message, nyt_settings.EMAIL_SENDER,
            [context['user'].email], connection=connection
        )
        self.logger.info("Sending to: %s" % context['user'].email)
        email.send(fail_silently=False)

    def handle(self, *args, **options):
        # activate the language
        activate(settings.LANGUAGE_CODE)

        options.setdefault('daemon', False)
        options.setdefault('cron', False)
        options.setdefault('no_sys_exit', False)

        daemon = options['daemon']
        cron = options['cron']

        assert not (daemon and cron), "You cannot both choose cron and daemon options"

        self.logger = logging.getLogger('django_nyt')

        if not self.logger.handlers:
            if daemon:
                handler = logging.FileHandler(filename=options['log'])
            else:
                handler = logging.StreamHandler(self.stdout)
            self.logger.addHandler(handler)
            self.logger.setLevel(logging.INFO)

        self.logger.info("Starting django_nyt e-mail dispatcher")

        if not nyt_settings.SEND_EMAILS:
            print("E-mails disabled - quitting.")
            sys.exit()

        # Run as daemon, ie. fork the process
        if daemon:
            self.logger.info("Daemon mode enabled, forking")
            try:
                fpid = os.fork()
                if fpid > 0:
                    # Running as daemon now. PID is fpid
                    self.logger.info("PID: %s" % str(fpid))
                    pid_file = open(options['pid'], "w")
                    pid_file.write(str(fpid))
                    pid_file.close()
                    if not options['no_sys_exit']:
                        sys.exit(0)
            except OSError as e:
                sys.stderr.write(
                    "fork failed: %d (%s)\n" %
                    (e.errno, e.strerror))
                sys.exit(1)

        # create a connection to smtp server for reuse
        try:
            connection = mail.get_connection()
        except:
            self.logger.error("Could get a mail connection")
            raise

        if cron:
            self.send_mails(connection)
        else:
            if not daemon:
                print("Entering send-loop, CTRL+C to exit")
            try:
                self.send_loop(connection, int(options['sleep_time']))
            except KeyboardInterrupt:
                print("\nQuitting...")

        # deactivate the language
        deactivate()

    def send_loop(self, connection, sleep_time):

        # This could be /improved by looking up the last notified person
        last_sent = None

        while True:

            started_sending_at = datetime.now()
            self.logger.info(
                "Starting send loop at %s" %
                str(started_sending_at))
            if last_sent:
                user_settings = models.Settings.objects.filter(
                    interval__lte=(
                        (started_sending_at -
                         last_sent).seconds //
                        60) //
                    60).order_by('user')
            else:
                user_settings = None

            self.send_mails(connection, last_sent=last_sent, user_settings=user_settings)

            connection.close()
            last_sent = datetime.now()
            elapsed_seconds = (last_sent - started_sending_at).seconds
            time.sleep(
                max(
                    (min(nyt_settings.INTERVALS)[0] - elapsed_seconds) * 60,
                    sleep_time,
                    0
                )
            )

    def send_mails(self, connection, last_sent=None, user_settings=None):
        """
        Does the lookups and sends out email digests to anyone who has them due.
        """

        self.logger.debug("Entering send_mails()")

        try:
            connection.open()
        except:
            self.logger.error("Could not use e-mail connection")
            raise

        if not user_settings:
            user_settings = models.Settings.objects.all().order_by('user')

        context = {'user': None,
                   'username': None,
                   'notifications': None,
                   'digest': None,
                   'site': Site.objects.get_current()}

        for setting in user_settings:
            context['user'] = setting.user
            context['username'] = getattr(setting.user, setting.user.USERNAME_FIELD)
            context['notifications'] = []
            # get the index of the tuple corresponding to the interval and
            # get the string name
            context[
                'digest'] = nyt_settings.INTERVALS[
                [y[0] for y in nyt_settings.INTERVALS].index(setting.
                                                             interval)][
                1]
            for subscription in setting.subscription_set.filter(
                send_emails=True,
                latest__is_emailed=False
            ):
                context['notifications'].append(subscription.latest)
            if len(context['notifications']) > 0:
                # STMP connection send loop
                while True:
                    try:
                        self._send_user_notifications(context, connection)
                        for n in context['notifications']:
                            n.is_emailed = True
                            n.save()
                        break
                    except smtplib.SMTPSenderRefused:
                        self.logger.error(
                            "E-mail refused by SMTP server ({}), skipping!".format(setting.user.email))
                        continue
                    except smtplib.SMTPException as e:
                        self.logger.error(
                            "You have an error with your SMTP server connection, error is: {}".format(e))
                        self.logger.error("Sleeping for 30s then retrying...")
                        time.sleep(30)
                    except Exception as e:
                        self.logger.error(
                            "Unhandled exception while sending, giving up: {}".format(e))
                        break

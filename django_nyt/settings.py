from __future__ import absolute_import
from __future__ import unicode_literals
from django.conf import settings as django_settings
from django import VERSION as DJANGO_VERSION
from django.utils.translation import ugettext_lazy as _


DB_TABLE_PREFIX = 'nyt'

# You need to switch this setting on, otherwise nothing will happen :)
ENABLED = getattr(django_settings, 'NYT_ENABLED', True)

# Enable django-admin registration
ENABLE_ADMIN = getattr(django_settings, 'NYT_ENABLE_ADMIN', False)

# Email notifications won't get sent unless you run
# python manage.py notifymail
SEND_EMAILS = getattr(django_settings, 'NYT_SEND_EMAILS', True)

EMAIL_SUBJECT = getattr(django_settings,
                        'NYT_EMAIL_SUBJECT', _("You have new notifications"))

EMAIL_SENDER = getattr(django_settings,
                       'NYT_EMAIL_SENDER', "notifications@example.com")

# Seconds to sleep between each database poll
# (leave high unless you really want to send extremely real time
# notifications)
NYT_SLEEP_TIME = 120

# You can always make up more numbers... they simply identify which notifications
# to send when invoking the script, and the number indicates how many hours
# to minimum pass between each notification.
INSTANTLY = 0
# Subtract 1, because the job finishes less than 24h before the next...
DAILY = (24 - 1) * 60
WEEKLY = 7 * (24 - 1) * 60

# List of intervals available. In minutes
INTERVALS = getattr(django_settings, 'NYT_INTERVALS',
                    [(INSTANTLY, _('instantly')),
                     (DAILY, _('daily')),
                        (WEEKLY, _('weekly'))]
                    )

INTERVALS_DEFAULT = INSTANTLY

# Django 1.5+
if DJANGO_VERSION >= (1, 5):
    USER_MODEL = getattr(django_settings, 'AUTH_USER_MODEL', 'auth.User')
else:
    USER_MODEL = 'auth.User'

NYT_LOG = getattr(django_settings, 'NYT_LOG', '/tmp/nyt_daemon.log')
NYT_PID = getattr(django_settings, 'NYT_PID', '/tmp/nyt_daemon.pid')

####################
# PLANNED SETTINGS #
####################

# Minimum logging and digital garbage! Don't save too much crap!

# After how many days should viewed notifications be deleted?
AUTO_DELETE = getattr(django_settings, 'NYT_AUTO_DELETE', 120)

# After how many days should all types of notifications be deleted?
AUTO_DELETE_ALL = getattr(django_settings, 'NYT_AUTO_DELETE_ALL', 120)

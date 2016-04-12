from __future__ import absolute_import
from __future__ import unicode_literals
from django.conf import settings as django_settings
from django import VERSION as DJANGO_VERSION
from django.utils.translation import ugettext_lazy as _

DB_TABLE_PREFIX = 'nyt'

# : Global setting to force-fully disable all propagation and creation of
# : notifications.
ENABLED = getattr(django_settings, 'NYT_ENABLED', True)

# : Enable django-admin registration for django-nyt's ModelAdmin's
ENABLE_ADMIN = getattr(django_settings, 'NYT_ENABLE_ADMIN', False)

# : Email notifications global setting, can be used to globally switch off
# : emails, both instant and scheduled digests.
# : Remeber that emails are sent with ``python manage.py notifymail``.
SEND_EMAILS = getattr(django_settings, 'NYT_SEND_EMAILS', True)

# : Subject of all emails sent
EMAIL_SUBJECT = getattr(django_settings,
                        'NYT_EMAIL_SUBJECT', _("You have new notifications"))

# : Default sender email
EMAIL_SENDER = getattr(django_settings,
                       'NYT_EMAIL_SENDER', "notifications@example.com")

# : Seconds to sleep between each database poll
# : (leave high unless you really want to send extremely real time
# : notifications)
NYT_SLEEP_TIME = 120

# You can always make up more numbers... they simply identify which notifications
# to send when invoking the script, and the number indicates how many hours
# to minimum pass between each notification.
INSTANTLY = 0
# Subtract 1, because the job finishes less than 24h before the next...
DAILY = (24 - 1) * 60
WEEKLY = 7 * (24 - 1) * 60

# : List of intervals available for user selections. In minutes
INTERVALS = getattr(
    django_settings,
    'NYT_INTERVALS',
    [
        (INSTANTLY, _('instantly')),
        (DAILY, _('daily')),
        (WEEKLY, _('weekly'))
    ]
)

# : Default selection for new subscriptions
INTERVALS_DEFAULT = INSTANTLY

USER_MODEL = getattr(django_settings, 'AUTH_USER_MODEL', 'auth.User')


############
# CHANNELS #
############

# : Channels are enabled automatically when 'channels' application is installed,
# : however you can explicitly disable it with NYT_CHANNELS_DISABLE.
ENABLE_CHANNELS = (
    'channels' in django_settings.INSTALLED_APPS and
    not getattr(django_settings, 'NYT_CHANNELS_DISABLE', False)
)

# Name of the global channel (preliminary stuff) that alerts everyone that there
# is a new notification
NOTIFICATION_CHANNEL = "nyt_all"


####################
# PLANNED SETTINGS #
####################

# : After how many days should viewed notifications be deleted? (not implemented)
AUTO_DELETE = getattr(django_settings, 'NYT_AUTO_DELETE', 120)

# : After how many days should both viewed and unviewed notifications be deleted? (not implemented)
AUTO_DELETE_ALL = getattr(django_settings, 'NYT_AUTO_DELETE_ALL', 120)

from django.conf import settings as django_settings
from django.utils.translation import gettext_lazy as _

DB_TABLE_PREFIX = "nyt"

ENABLED = getattr(django_settings, "NYT_ENABLED", True)
"""Global setting to force-fully disable all propagation and creation of
notifications."""

ENABLE_ADMIN = getattr(django_settings, "NYT_ENABLE_ADMIN", False)
"""Enable django-admin registration for django-nyt's ModelAdmin's"""

SEND_EMAILS = getattr(django_settings, "NYT_SEND_EMAILS", True)
"""Email notifications global setting, can be used to globally switch off
emails, both instant and scheduled digests.
Remeber that emails are sent with ``python manage.py notifymail``."""

EMAIL_SUBJECT = getattr(
    django_settings, "NYT_EMAIL_SUBJECT", _("You have new notifications")
)
"""Subject of all emails sent"""

EMAIL_SENDER = getattr(django_settings, "NYT_EMAIL_SENDER", "notifications@example.com")
"""Default sender email"""

# You can always make up more numbers... they simply identify which notifications
# to send when invoking the script, and the number indicates how many hours
# to minimum pass between each notification.
INSTANTLY = 0
# Subtract 1, because the job finishes less than 24h before the next...
DAILY = (24 - 1) * 60
WEEKLY = 7 * (24 - 1) * 60

INTERVALS = getattr(
    django_settings,
    "NYT_INTERVALS",
    [(INSTANTLY, _("instantly")), (DAILY, _("daily")), (WEEKLY, _("weekly"))],
)
"""List of intervals available for user selections. In minutes"""

INTERVALS_DEFAULT = INSTANTLY
"""Default selection for new subscriptions"""

USER_MODEL = getattr(django_settings, "AUTH_USER_MODEL", "auth.User")


############
# CHANNELS #
############

ENABLE_CHANNELS = "channels" in django_settings.INSTALLED_APPS and not getattr(
    django_settings, "NYT_CHANNELS_DISABLE", False
)
"""Channels are enabled automatically when 'channels' application is installed,
however you can explicitly disable it with NYT_CHANNELS_DISABLE."""

# Name of the global channel (preliminary stuff) that alerts everyone that there
# is a new notification
NOTIFICATION_CHANNEL = "nyt_all-{notification_key:s}"


####################
# PLANNED SETTINGS #
####################

# AUTO_DELETE = getattr(django_settings, 'NYT_AUTO_DELETE', 120)
"""After how many days should viewed notifications be deleted? (not implemented)"""

# AUTO_DELETE_ALL = getattr(django_settings, 'NYT_AUTO_DELETE_ALL', 120)
"""After how many days should both viewed and unviewed notifications be deleted? (not implemented)"""

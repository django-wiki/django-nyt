"""
These are the default settings from ``django_nyt.settings`` that can be overridden from
your Django project's settings module by defining a setting with the same name.
"""
from collections import OrderedDict

from django.conf import settings as django_settings
from django.utils.translation import gettext_lazy as _

NYT_DB_TABLE_PREFIX = "nyt"
"""The table prefix for tables in the database. Do not change this unless you know what you are doing."""

NYT_ENABLED = True
"""Global setting to force-fully disable all propagation and creation of
notifications."""

NYT_ENABLE_ADMIN = False
"""Enable django-admin registration for django-nyt's ModelAdmin classes."""

NYT_SEND_EMAILS = True
"""Email notifications global setting, can be used to globally switch off
emails, both instant and scheduled digests.
Remember that emails are sent with ``python manage.py notifymail``."""

NYT_EMAIL_SUBJECT = None
"""Hard-code a subject for all emails sent (overrides the default subject templates)."""

NYT_EMAIL_SENDER = "notifications@example.com"
"""Default sender email for notification emails. You should definitely make this match
an email address that your email gateway will allow you to send from. You may also
consider a no-reply kind of email if your notification system has a UI for changing
notification settings."""

EMAIL_TEMPLATE_DEFAULT = "notifications/emails/default.txt"
EMAIL_SUBJECT_TEMPLATE_DEFAULT = "notifications/emails/default_subject.txt"

NYT_EMAIL_TEMPLATE_NAMES = OrderedDict()
"""Default dictionary, mapping notification keys to template names. Can be overwritten by database values.
Keys can have a glob pattern, like USER_CHANGED_*."""

NYT_EMAIL_SUBJECT_TEMPLATE_NAMES = OrderedDict()
"""Default dictionary, mapping notification keys to template names. The templates are used to generate a single-line email subject.
Can be overwritten by database values.
Keys can have a glob pattern, like ``USER_CHANGED_*.``"""

# You can always make up more numbers... they simply identify which notifications
# to send when invoking the script, and the number indicates how many hours
# to minimum pass between each notification.
INSTANTLY = 0
# Subtract 1, because the job finishes less than 24h before the next...
DAILY = (24 - 1) * 60
WEEKLY = 7 * (24 - 1) * 60

NYT_INTERVALS = [
    (INSTANTLY, _("instantly")),
    (DAILY, _("daily")),
    (WEEKLY, _("weekly")),
]
"""List of intervals available for user selections. In minutes"""

NYT_INTERVALS_DEFAULT = INSTANTLY
"""Default selection for new subscriptions"""

NYT_USER_MODEL = getattr(django_settings, "AUTH_USER_MODEL", "auth.User")
"""The swappable user model of Django Nyt. The default is to use the contents of ``AUTH_USER_MODEL``."""

############
# CHANNELS #
############

NYT_ENABLE_CHANNELS = "channels" in django_settings.INSTALLED_APPS and not getattr(
    django_settings, "NYT_CHANNELS_DISABLE", False
)
"""Channels are enabled automatically when 'channels' application is installed,
however you can explicitly disable it with NYT_CHANNELS_DISABLE."""

# Name of the global channel (preliminary stuff) that alerts everyone that there
# is a new notification
NYT_NOTIFICATION_CHANNEL = "nyt_all-{notification_key:s}"

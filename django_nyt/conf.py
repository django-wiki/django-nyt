"""
These are the available settings, accessed through ``django_nyt.conf.app_settings``.
All attributes prefixed ``NYT_*`` can be overridden from your Django project's settings module by defining a setting with the same name.

For instance, to enable the admin, add the following to your project settings:

.. code-block:: python

    NYT_ENABLE_ADMIN = True
"""
from __future__ import annotations

from collections import OrderedDict
from dataclasses import dataclass
from dataclasses import field
from typing import Any

from django.conf import settings as django_settings
from django.utils.translation import gettext_lazy as _

# All attributes accessed with this prefix are possible to overwrite
# through django.conf.settings.
settings_prefix = "NYT_"

INSTANTLY = 0
# Subtract 1, because the job finishes less than 24h before the next...
DAILY = (24 - 1) * 60
WEEKLY = 7 * (24 - 1) * 60


@dataclass(frozen=True)
class AppSettings:
    """Access this instance as ``django_nyt.conf.app_settings``."""

    NYT_DB_TABLE_PREFIX: str = "nyt"
    """The table prefix for tables in the database. Do not change this unless you know what you are doing."""

    NYT_ENABLE_ADMIN: bool = False
    """Enable django-admin registration for django-nyt's ModelAdmin classes."""

    NYT_SEND_EMAILS: bool = True
    """Email notifications global setting, can be used to globally switch off
    emails, both instant and scheduled digests.
    Remember that emails are sent with ``python manage.py notifymail``."""

    NYT_EMAIL_SUBJECT: str = None
    """Hard-code a subject for all emails sent (overrides the default subject templates)."""

    NYT_EMAIL_SENDER: str = "notifications@example.com"
    """Default sender email for notification emails. You should definitely make this match
    an email address that your email gateway will allow you to send from. You may also
    consider a no-reply kind of email if your notification system has a UI for changing
    notification settings."""

    NYT_EMAIL_TEMPLATE_DEFAULT: str = "notifications/emails/default.txt"
    """Default template used for rendering email contents.
    Should contain a valid template name.
    If a lookup in ``NYT_EMAIL_TEMPLATE_NAMES`` doesn't return a result, this fallback is used."""

    NYT_EMAIL_SUBJECT_TEMPLATE_DEFAULT: str = "notifications/emails/default_subject.txt"
    """Default template used for rendering the email subject.
    Should contain a valid template name.
    If a lookup in ``NYT_EMAIL_SUBJECT_TEMPLATE_NAMES`` doesn't return a result, this fallback is used."""

    NYT_EMAIL_TEMPLATE_NAMES: dict = field(default_factory=OrderedDict)
    """Default dictionary, mapping notification keys to template names. Can be overwritten by database values.
    Keys can have a glob pattern, like ``USER_*`` or ``user/*``.

    When notification emails are generated,
    they are grouped by their templates such that notifications sharing the same template can be sent in a combined email.

    Example:

    .. code-block:: python

        NYT_EMAIL_TEMPLATE_NAMES = OrderedDict(
            [
                ("admin/product/created", "myapp/notifications/email/admin_product_added.txt"),
                ("admin/**", "myapp/notifications/email/admin_default.txt"),
            ]
        )
    """

    NYT_EMAIL_SUBJECT_TEMPLATE_NAMES: dict = field(default_factory=OrderedDict)
    """Default dictionary, mapping notification keys to template names. The templates are used to generate a single-line email subject.
    Can be overwritten by database values.
    Keys can have a glob pattern, like ``USER_*`` or ``user/*``.

    When notification emails are generated,
    they are grouped by their templates such that notifications sharing the same template can be sent in a combined email.

    Example:

    .. code-block:: python

        NYT_EMAIL_SUBJECT_TEMPLATE_NAMES = OrderedDict(
            [
                ("admin/product/created", "myapp/notifications/email/admin_product_added.txt"),
                ("admin/**", "myapp/notifications/email/admin_default.txt"),
            ]
        )
    """

    NYT_INTERVALS: list[tuple[int, Any]] | tuple[tuple[int, Any]] = (
        (INSTANTLY, _("instantly")),
        (DAILY, _("daily")),
        (WEEKLY, _("weekly")),
    )
    """List of intervals available for user selections. In minutes"""

    NYT_INTERVALS_DEFAULT: int = INSTANTLY
    """Default selection for new subscriptions"""

    NYT_USER_MODEL: str = getattr(django_settings, "AUTH_USER_MODEL", "auth.User")
    """The swappable user model of Django Nyt. The default is to use the contents of ``AUTH_USER_MODEL``."""

    ############
    # CHANNELS #
    ############

    NYT_ENABLE_CHANNELS: str = (
        "channels" in django_settings.INSTALLED_APPS
        and not getattr(django_settings, "NYT_CHANNELS_DISABLE", False)
    )
    """Channels are enabled automatically when 'channels' application is installed,
    however you can explicitly disable it with NYT_CHANNELS_DISABLE."""

    # Name of the global channel (preliminary stuff) that alerts everyone that there
    # is a new notification
    NYT_NOTIFICATION_CHANNEL: str = "nyt_all-{notification_key:s}"

    def __getattribute__(self, __name: str) -> Any:
        """
        Check if a Django project settings should override the app default.

        In order to avoid returning any random properties of the django settings, we inspect the prefix firstly.
        """

        if __name.startswith(settings_prefix) and hasattr(django_settings, __name):
            return getattr(django_settings, __name)

        return super().__getattribute__(__name)


app_settings = AppSettings()

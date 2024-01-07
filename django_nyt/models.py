import re

from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from django.db.models.signals import post_delete
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from django_nyt.conf import app_settings

_notification_type_cache = {}


def _glob_matches_path(glob_pattern, path):
    """
    Matches a glob pattern with a string. This is apparently not something that's available in Python's stdlib.

    Examples::

        _glob_matches_path("admin/*", "admin/user/new") == False
        _glob_matches_path("admin/**", "admin/user/new") == True
    """
    return bool(re.compile(_glob_to_re(glob_pattern)).match(path))


def _glob_to_re(pat: str) -> str:  # noqa: max-complexity=15
    """Translate a shell PATTERN to a regular expression.

    Copied from: https://stackoverflow.com/a/72400344/405682
    """

    i, n = 0, len(pat)
    res = ""
    while i < n:
        c = pat[i]
        i = i + 1
        if c == "*":
            # -------- CHANGE START --------
            # prevent '*' matching directory boundaries, but allow '**' to match them
            j = i
            if j < n and pat[j] == "*":
                res = res + ".*"
                i = j + 1
            else:
                res = res + "[^/]*"
            # -------- CHANGE END ----------
        elif c == "?":
            # -------- CHANGE START --------
            # prevent '?' matching directory boundaries
            res = res + "[^/]"
            # -------- CHANGE END ----------
        elif c == "[":
            j = i
            if j < n and pat[j] == "!":
                j = j + 1
            if j < n and pat[j] == "]":
                j = j + 1
            while j < n and pat[j] != "]":
                j = j + 1
            if j >= n:
                res = res + "\\["
            else:
                stuff = pat[i:j]
                if "--" not in stuff:
                    stuff = stuff.replace("\\", r"\\")
                else:
                    chunks = []
                    k = i + 2 if pat[i] == "!" else i + 1
                    while True:
                        k = pat.find("-", k, j)
                        if k < 0:
                            break
                        chunks.append(pat[i:k])
                        i = k + 1
                        k = k + 3
                    chunks.append(pat[i:j])
                    # Escape backslashes and hyphens for set difference (--).
                    # Hyphens that create ranges shouldn't be escaped.
                    stuff = "-".join(
                        s.replace("\\", r"\\").replace("-", r"\-") for s in chunks
                    )
                # Escape set operations (&&, ~~ and ||).
                stuff = re.sub(r"([&~|])", r"\\\1", stuff)
                i = j + 1
                if stuff[0] == "!":
                    # -------- CHANGE START --------
                    # ensure sequence negations don't match directory boundaries
                    stuff = "^/" + stuff[1:]
                    # -------- CHANGE END ----------
                elif stuff[0] in ("^", "["):
                    stuff = "\\" + stuff
                res = "%s[%s]" % (res, stuff)
        else:
            res = res + re.escape(c)
    return r"(?s:%s)\Z" % res


class NotificationType(models.Model):
    """
    Notification types are added on-the-fly by the
    applications adding new notifications
    """

    key = models.CharField(
        max_length=128, primary_key=True, verbose_name=_("unique key"), unique=True
    )

    # TODO: This isn't translatable
    label = models.CharField(
        max_length=128, verbose_name=_("optional label"), blank=True, null=True
    )

    content_type = models.ForeignKey(
        ContentType, blank=True, null=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.key

    class Meta:
        db_table = app_settings.NYT_DB_TABLE_PREFIX + "_notificationtype"
        verbose_name = _("type")
        verbose_name_plural = _("types")

    @classmethod
    def get_by_key(cls, key, content_type=None):

        if key in _notification_type_cache:
            return _notification_type_cache[key]

        try:
            nt = cls.objects.get(key=key)
        except cls.DoesNotExist:
            nt = cls.objects.create(key=key, content_type=content_type)
        _notification_type_cache[key] = nt
        return nt

    def get_email_template_name(self):
        for key_glob, template_name in app_settings.NYT_EMAIL_TEMPLATE_NAMES.items():
            if _glob_matches_path(key_glob, self.key):
                return template_name
        return app_settings.NYT_EMAIL_TEMPLATE_DEFAULT

    def get_email_subject_template_name(self):
        for (
            key_glob,
            template_name,
        ) in app_settings.NYT_EMAIL_SUBJECT_TEMPLATE_NAMES.items():
            if _glob_matches_path(key_glob, self.key):
                return template_name
        return app_settings.NYT_EMAIL_SUBJECT_TEMPLATE_DEFAULT


@receiver([post_save, post_delete], sender=NotificationType)
def clear_notification_type_cache(*args, **kwargs):
    global _notification_type_cache
    _notification_type_cache = {}


class Settings(models.Model):
    """
    Reusable settings object for a subscription
    """

    user = models.ForeignKey(
        app_settings.NYT_USER_MODEL,
        on_delete=models.CASCADE,  # If a user is deleted, remove all settings
        verbose_name=_("user"),
        related_name="nyt_settings",
    )

    interval = models.SmallIntegerField(
        choices=app_settings.NYT_INTERVALS,
        verbose_name=_("interval"),
        help_text=_("interval in minutes (0=instant, 60=notify once per hour)"),
        default=app_settings.NYT_INTERVALS_DEFAULT,
    )

    is_default = models.BooleanField(
        default=False,
        verbose_name=_("Default for new subscriptions"),
    )

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("created"),
    )

    modified = models.DateTimeField(
        auto_now=True,
        verbose_name=_("modified"),
    )

    def __str__(self):
        obj_name = _("Settings for %s") % getattr(self.user, self.user.USERNAME_FIELD)
        return obj_name

    class Meta:
        db_table = app_settings.NYT_DB_TABLE_PREFIX + "_settings"
        verbose_name = _("settings")
        verbose_name_plural = _("settings")

    def clean(self):
        if not self.is_default and self.pk and self.user:
            default_settings = Settings.objects.filter(
                user=self.user,
                is_default=True,
            ).exclude(pk=self.pk)
            if not default_settings.exists():
                raise ValidationError(
                    _("At minimum one default setting must exist for the user")
                )

    def save(self, *args, **kwargs):
        # We should check that it's the only default setting manually because
        # it's not possible to create a database constraint for this.
        # Instead of having a constraint, we unset all other is_default for
        # the user.
        default_settings = Settings.objects.filter(
            user=self.user,
            is_default=True,
        ).exclude(pk=self.pk)
        if self.is_default:
            default_settings.update(is_default=False)
        elif not default_settings.exists():
            non_default_settings = Settings.objects.filter(
                user=self.user,
                is_default=False,
            ).exclude(pk=self.pk)
            if non_default_settings.exists():
                non_default_settings[0].is_default = True
                non_default_settings[0].save()
            else:
                raise ValueError("A user must have a default settings object")
        super(Settings, self).save(*args, **kwargs)

    @classmethod
    def get_default_settings(cls, user):
        return cls.objects.get_or_create(user=user, is_default=True)[0]

    # Fixes an old typo.
    get_default_setting = get_default_settings


class Subscription(models.Model):

    # If settings are deleted, remove all subscriptions (CASCADE)
    settings = models.ForeignKey(
        Settings,
        verbose_name=_("settings"),
        on_delete=models.CASCADE,
    )

    notification_type = models.ForeignKey(
        NotificationType, verbose_name=_("notification type"), on_delete=models.CASCADE
    )

    object_id = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        help_text=_("Leave this blank to subscribe to any kind of object"),
        verbose_name=_("object ID"),
    )

    send_emails = models.BooleanField(
        default=True,
        verbose_name=_("send emails"),
    )

    latest = models.ForeignKey(
        "Notification",
        null=True,
        blank=True,
        related_name="latest_for",
        verbose_name=_("latest notification"),
        on_delete=models.CASCADE,
    )

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("created"),
    )

    modified = models.DateTimeField(
        auto_now=True,
        verbose_name=_("modified"),
    )

    last_sent = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_("last sent"),
    )

    def __str__(self):
        obj_name = _("Subscription for: %s") % (
            getattr(self.settings.user, self.settings.user.USERNAME_FIELD)
        )
        return obj_name

    class Meta:
        db_table = app_settings.NYT_DB_TABLE_PREFIX + "_subscription"
        verbose_name = _("subscription")
        verbose_name_plural = _("subscriptions")


class Notification(models.Model):

    #: Either set the subscription
    subscription = models.ForeignKey(
        Subscription,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_("subscription"),
    )

    #: Or the user to receive the notification
    # If a user is deleted, remove all notifications (CASCADE)
    user = models.ForeignKey(
        app_settings.NYT_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name=_("user"),
        related_name="nyt_notifications",
    )

    message = models.TextField()

    # https://stackoverflow.com/a/417184/405682
    url = models.CharField(
        verbose_name=_("link for notification"),
        blank=True,
        null=True,
        max_length=2000,
    )

    is_viewed = models.BooleanField(
        default=False,
        verbose_name=_("notification viewed"),
    )

    is_emailed = models.BooleanField(
        default=False,
        verbose_name=_("mail sent"),
    )

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("created"),
    )

    modified = models.DateTimeField(
        auto_now=True,
        verbose_name=_("modified"),
    )

    occurrences = models.PositiveIntegerField(
        default=1,
        verbose_name=_("occurrences"),
        help_text=_(
            "If the same notification was fired multiple "
            "times with no intermediate notifications"
        ),
    )

    def save(self, *args, **kwargs):
        assert self.user or self.subscription
        if not self.user:
            self.user = self.subscription.settings.user
        super(Notification, self).save(*args, **kwargs)

    @classmethod
    def create_notifications(
        cls,
        key,
        object_id=None,
        content_type=None,
        filter_exclude=None,
        recipient_users=None,
        **kwargs
    ):
        """
        Creates notifications directly in database -- do not call directly,
        use django_nyt.notify(...)

        This is now an internal interface.
        """

        if not key or not isinstance(key, str):
            raise KeyError("No notification key (string) specified.")

        if filter_exclude is None:
            filter_exclude = {}

        objects_created = []
        subscriptions = Subscription.objects.filter(notification_type__key=key).exclude(
            **filter_exclude
        )

        # TODO: This query should include notification_type__content_type? Why was this not added?
        if object_id:
            subscriptions = subscriptions.filter(
                Q(object_id=object_id) | Q(object_id=None)
            )
        if recipient_users:
            subscriptions = subscriptions.filter(
                settings__user__in=recipient_users,
            )

        subscriptions = subscriptions.prefetch_related("latest", "settings")
        subscriptions = subscriptions.order_by("settings__user")

        seen_key_for_settings = {}

        for subscription in subscriptions:
            # Don't alert the same user several times even though overlapping
            # subscriptions occur.
            # TODO: This is problematic for users that have complex configurations.
            # It should be made configurable.
            # if subscription.settings.user == prev_user:
            #     continue

            # If this settings has already been notified in this loop, then continue.
            # This happens when there are several overlapping subscriptions for the same key.
            seen_key_for_settings.setdefault(subscription.settings.id, [])
            if key in seen_key_for_settings[subscription.settings.id]:
                continue

            seen_key_for_settings[subscription.settings.id].append(key)

            # Check if it's the same as the previous message
            latest = subscription.latest
            if latest and (
                latest.message == kwargs.get("message", None)
                and latest.url == kwargs.get("url", None)
                and latest.is_viewed is False
            ):
                # Both message and URL are the same, and it hasn't been viewed
                # so just increment occurrence count.
                latest.occurrences = latest.occurrences + 1
                latest.is_emailed = False
                latest.save()
            else:
                # Insert a new notification
                new_obj = cls.objects.create(subscription=subscription, **kwargs)
                objects_created.append(new_obj)
                subscription.latest = new_obj
                subscription.save()

        return objects_created

    def __str__(self):
        return "%s: %s" % (self.user, self.message)

    class Meta:
        db_table = app_settings.NYT_DB_TABLE_PREFIX + "_notification"
        verbose_name = _("notification")
        verbose_name_plural = _("notifications")
        ordering = ("-id",)

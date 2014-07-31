# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _

from django.contrib.contenttypes.models import ContentType

from django_nyt import settings


_notification_type_cache = {}


class NotificationType(models.Model):

    """
    Notification types are added on-the-fly by the
    applications adding new notifications
    """
    key = models.CharField(
        max_length=128,
        primary_key=True,
        verbose_name=_('unique key'),
        unique=True
    )
    label = models.CharField(
        max_length=128,
        verbose_name=_('optional label'),  # TODO: This isn't translatable, why do we have it!?
        blank=True,
        null=True
    )
    content_type = models.ForeignKey(ContentType, blank=True, null=True)

    def __unicode__(self):
        return self.key

    class Meta:
        db_table = settings.DB_TABLE_PREFIX + '_notificationtype'
        verbose_name = _('type')
        verbose_name_plural = _('types')
    
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


class Settings(models.Model):

    """
    Reusable settings object for a subscription
    """

    user = models.ForeignKey(
        settings.USER_MODEL,
        on_delete=models.CASCADE,  # If a user is deleted, remove all settings
        verbose_name=_(u"user"),
    )
    interval = models.SmallIntegerField(
        choices=settings.INTERVALS,
        verbose_name=_('interval'),
        default=settings.INTERVALS_DEFAULT,
    )

    def __unicode__(self):
        obj_name = _("Settings for %s") % self.user.username
        return unicode(obj_name)

    class Meta:
        db_table = settings.DB_TABLE_PREFIX + '_settings'
        verbose_name = _('settings')
        verbose_name_plural = _('settings')


class Subscription(models.Model):

    settings = models.ForeignKey(
        Settings,
        verbose_name=_(u"settings"),
        on_delete=models.CASCADE,  # If settings are deleted, remove all subscriptions
    )
    notification_type = models.ForeignKey(
        NotificationType,
        verbose_name=_(u"notification type"),
    )
    object_id = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        help_text=_('Leave this blank to subscribe to any kind of object'),
        verbose_name=_(u"object ID"),
    )
    send_emails = models.BooleanField(
        default=True,
        verbose_name=_(u"send emails"),
    )
    latest = models.ForeignKey(
        'Notification',
        null=True,
        blank=True,
        related_name='latest_for',
        verbose_name=_(u"latest notification"),
    )

    def __unicode__(self):
        obj_name = _("Subscription for: %s") % unicode(self.settings.user.username)
        return unicode(obj_name)

    class Meta:
        db_table = settings.DB_TABLE_PREFIX + '_subscription'
        verbose_name = _('subscription')
        verbose_name_plural = _('subscriptions')


class Notification(models.Model):
    
    # Either set the subscription
    subscription = models.ForeignKey(
        Subscription,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_(u"subscription"),
    )
    # Or the user to receive the notification
    user = models.ForeignKey(
        'auth.User',
        null=True,
        blank=True,
        on_delete=models.CASCADE,  # If a user is deleted, remove all notifications
        verbose_name=_(u"user"),
    )
    message = models.TextField()
    url = models.CharField(
        verbose_name=_('link for notification'),
        blank=True,
        null=True,
        max_length=200,  # TODO: Why 200?
    )
    is_viewed = models.BooleanField(default=False)
    is_emailed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    occurrences = models.PositiveIntegerField(
        default=1,
        verbose_name=_('occurrences'),
        help_text=_(
            'If the same notification was fired multiple '
            'times with no intermediate notifications'
        ),
    )
    
    def save(self, *args, **kwargs):
        assert self.user or self.subscription
        if not self.user:
            self.user = self.subscription.settings.user
        super(Notification, self).save(*args, **kwargs)

    @classmethod
    def create_notifications(cls, key, **kwargs):
        """Creates notifications directly in database -- do not call directly, use django_nyt.notify(...)"""
        if not key or not isinstance(key, str):
            raise KeyError('No notification key (string) specified.')

        object_id = kwargs.pop('object_id', None)
        filter_exclude = kwargs.pop('filter_exclude', {})
        recipient_users = kwargs.pop('recipient_users', None)

        objects_created = []
        subscriptions = Subscription.objects.filter(
            notification_type__key=key,
            **filter_exclude
        )
        if object_id:
            subscriptions = subscriptions.filter(
                Q(object_id=object_id) |
                Q(object_id=None)
            )
        if recipient_users:
            subscriptions = subscriptions.filter(
                settings__user__in=recipient_users,
            )

        subscriptions = subscriptions.prefetch_related('latest', 'settings')
        subscriptions = subscriptions.order_by('settings__user')
        prev_user = None

        for subscription in subscriptions:
            # Don't alert the same user several times even though overlapping
            # subscriptions occur.
            if subscription.settings.user == prev_user:
                continue

            # Check if it's the same as the previous message
            latest = subscription.latest
            if latest and (latest.message == kwargs.get('message', None) and
                           latest.url == kwargs.get('url', None) and
                           latest.is_viewed is False):
                # Both message and URL are the same, and it hasn't been viewed
                # so just increment occurrence count.
                latest.occurrences = latest.occurrences + 1
                latest.is_emailed = False
                latest.save()
            else:
                # Insert a new notification
                new_obj = cls.objects.create(
                    subscription=subscription,
                    **kwargs)
                objects_created.append(
                    new_obj
                )
                subscription.latest = new_obj
                subscription.save()
            prev_user = subscription.settings.user

        return objects_created

    def __unicode__(self):
        return "%s: %s" % (unicode(self.user), self.message)

    class Meta:
        db_table = settings.DB_TABLE_PREFIX + '_notification'
        verbose_name = _('notification')
        verbose_name_plural = _('notifications')
        ordering = ('-id',)

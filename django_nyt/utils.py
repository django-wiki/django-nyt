from django.db.models import Model
from django.utils.translation import gettext as _

from . import _disable_notifications
from . import models
from . import settings


def notify(
    message, key, target_object=None, url=None, filter_exclude={}, recipient_users=None
):
    """
    Notify subscribing users of a new event. Key can be any kind of string,
    just make sure to reuse it where applicable.

    notify("there was a response to your comment", "comment_response",
           target_object=PostersObject,
           url=reverse('comments:view', args=(PostersObject.id,)))

    The below example notifies everyone subscribing to the "new_comments" key
    with the message "New comment posted".

    notify("New comment posted", "new_comments")

    filter_exclude: a dictionary to exclude special elements of subscriptions
    in the queryset, for instance filter_exclude={''}

    :param: key <string>: Some identifier of your notification type
    :param: recipient_users: A possible iterable of users that should be notified
                             instead of notifying all subscribers of the event.
                             Notice that users still have to be actually subscribed
                             to the event key!
    :param: target_object: Any django model instance that this notification
                           relates to. User django content types.
    """

    if _disable_notifications:
        return 0

    if target_object:
        if not isinstance(target_object, Model):
            raise TypeError(
                _(
                    "You supplied a target_object that's not an instance of a django Model."
                )
            )
        object_id = target_object.id
    else:
        object_id = None

    objects = models.Notification.create_notifications(
        key,
        object_id=object_id,
        message=message,
        url=url,
        filter_exclude=filter_exclude,
        recipient_users=recipient_users,
    )

    # Notify channel subscribers if we have channels enabled
    if settings.ENABLE_CHANNELS:
        from django_nyt import subscribers

        subscribers.notify_subscribers(objects, key)

    return len(objects)


def subscribe(settings, key, content_type=None, object_id=None, **kwargs):
    """
    Creates a new subscription to a given key. If the key does not exist
    as a NotificationType, it will be created

    Uses get_or_create to avoid double creation
    See: https://docs.djangoproject.com/en/dev/ref/models/querysets/#get-or-create

    :param: settings: A models.Settings instance
    :param: key: The unique key that the Settings should subscribe to
    :param: content_type: If notifications are regarding a specific ContentType, it should be set
    :param: object_id: If the notifications should only regard a specific object_id
    :param: **kwargs: Additional models.Subscription field values
    """
    notification_type = models.NotificationType.get_by_key(
        key, content_type=content_type
    )

    return models.Subscription.objects.get_or_create(
        settings=settings,
        notification_type=notification_type,
        object_id=object_id,
        **kwargs
    )[0]

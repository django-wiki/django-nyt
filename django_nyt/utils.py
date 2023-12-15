from typing import Any
from typing import List
from typing import Tuple
from typing import Union

from django.contrib.contenttypes.models import ContentType
from django.db.models import Model
from django.utils.translation import gettext as _

import django_nyt
from . import models
from .conf import app_settings


def notify(
    message: str,
    key: str,
    target_object: Any = None,
    url: str = None,
    filter_exclude: dict = None,
    recipient_users: list = None,
) -> List[models.Notification]:
    """
    Notify subscribing users of a new event. Key can be any kind of string,
    just make sure to reuse it where applicable.

    Here is the most basic example: Everyone subscribing to the `"new_comments"` key
    are sent a notification with the message "New comment posted"::

        notify("New comment posted", "new_comments")

    Here is an example that will create a Notification object for everyone who
    has a subscription for the key `"comment/response"` and the model instance `comment_instance`.
    The idea would be that the poster of `comment_instance` will receive notifications when someone responds to that comment.

    .. code-block:: python

        notify(
            "there was a response to your comment",
            "comment/response",
            target_object=comment_instance,
            url=reverse('comments:view', args=(comment_instance.id,))
        )

    :param message: A string containing the message that should be sent to all subscribed users.
    :param key: A key object which is matched to ``NotificationType.key``.
                Users with a Subscription for that NotificationType will have a Notification object created.
    :param url: A URL pointing to your notification.
                If the URL is pointing to your Django project's unique website,
                then add an ``/absolute/url``. However, if the URL should take the user to a different website,
                use a full HTTP scheme, i.e. ``https://example.org/url/``.
    :param recipient_users: A possible iterable of users that should be notified
                            instead of notifying all subscribers of the event.
                            Notice that users still have to be actually subscribed
                            to the event key!
    :param target_object: Any Django model instance that this notification
                          relates to. Uses Django content types.
                          Subscriptions with a matching content_type and object_id will be notified.
    :param filter_exclude: Keyword arguments passed to filter out Subscriptions.
                           Will be handed to ``Subscription.objects.exclude(**filter_exclude)``.
    """

    if django_nyt._disable_notifications:
        return []

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

    notifications = models.Notification.create_notifications(
        key,
        object_id=object_id,
        message=message,
        url=url,
        filter_exclude=filter_exclude,
        recipient_users=recipient_users,
    )

    # Notify channel subscribers if we have channels enabled
    if app_settings.NYT_ENABLE_CHANNELS:
        from django_nyt import subscribers

        subscribers.notify_subscribers(notifications, key)

    return notifications


def subscribe(
    settings: models.Settings,
    key: str,
    content_type: Union[str, ContentType] = None,
    object_id: Union[int, str] = None,
    **kwargs
) -> models.Subscription:
    """
    Creates a new subscription to a given key. If the key does not exist
    as a NotificationType, it will be created

    Uses `get_or_create <https://docs.djangoproject.com/en/dev/ref/models/querysets/#get-or-create>`__
    to avoid double creation.

    :param settings: A models.Settings instance
    :param key: The unique key that the Settings should subscribe to
    :param content_type: If notifications are regarding a specific ContentType, it should be set
    :param object_id: If the notifications should only regard a specific object_id
    :param **kwargs: Additional models.Subscription field values
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


def unsubscribe(
    key: str,
    user: Any = None,
    settings: models.Settings = None,
    content_type: Union[str, ContentType] = None,
    object_id: Union[int, str] = None,
) -> Tuple[int, dict]:
    """
    Shortcut function to remove all subscriptions related to a notification key and either a user or a settings object.

    Unsubscribing does NOT delete old notifications, however the subscription relation is nullified.
    This means that any objects accessed through that relation will become inaccessible.
    This is a particular feature chosen to avoid accidentally allowing access to data that may be otherwise have credential-based access.

    :param key: The notification key to unsubscribe a user/user settings.
    :param user: User to unsubscribe
    :param settings: ...or a UserSettings object
    :param content_type: Further narrow down subscriptions to only this content_type
    :param object_id: Further narrow down subscriptions to only this object_id (provided a content_type)
    :return: (int, dict) - the return value of Django's queryset.delete() method.
    """

    assert not (user and settings), "Cannot apply both User and UserSettings object."
    assert (
        user or settings
    ), "Need at least a User and a UserSettings object, refusing to unsubscribe all."
    assert bool(content_type) == bool(
        object_id
    ), "You have to supply both a content_type and object_id or none of them."

    subscriptions = models.Subscription.objects.filter(
        notification_type__key=key,
    )

    if object_id and content_type:
        subscriptions = models.Subscription.objects.filter(
            notification_type__content_type=content_type,
            object_id=object_id,
        )
    else:
        subscriptions = models.Subscription.objects.filter(
            notification_type__content_type=None,
            object_id=None,
        )

    if user:
        subscriptions = subscriptions.filter(
            settings__user=user,
        )

    if settings:
        subscriptions = subscriptions.filter(
            settings=settings,
        )

    return subscriptions.delete()

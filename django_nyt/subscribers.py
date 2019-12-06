from logging import getLogger

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from . import models, settings

logger = getLogger(name=__name__)


def notify_subscribers(notifications, key):
    """
    Notify all open channels about new notifications
    """

    logger.debug("Broadcasting to subscribers")
    channel_layer = get_channel_layer()
    notification_type_ids = models.NotificationType.objects.values('key').filter(key=key)

    for notification_type in notification_type_ids:
        channel_name = settings.NOTIFICATION_CHANNEL.format(notification_key=notification_type['key'])
        async_to_sync(channel_layer.group_send)(channel_name, {'type': 'websocket.send', 'text': 'new-notification'})


def subscribe_channels(subscribe):
    """
    subscribe connected user on channels level
    """

    logger.debug("Broadcasting to subscribers")
    channel_layer = get_channel_layer()
    subscriber_room = 'nyt_personal-{}'.format(subscribe.settings.user.api_uuid)
    channel_name = settings.NOTIFICATION_CHANNEL.format(notification_key=subscribe.notification_type.key)

    async_to_sync(channel_layer.group_send)(subscriber_room, {'type': 'websocket.subscribe', "room": channel_name})

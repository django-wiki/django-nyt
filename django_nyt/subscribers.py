import logging

from channels.layers import get_channel_layer

from . import models, settings

logger = logging.getLogger(__name__)


def notify_subscribers(notifications, key):
    """
    Notify all open channels about new notifications
    """

    logger.debug("Broadcasting to subscribers")
    channel_layer = get_channel_layer()
    notification_type_ids = models.NotificationType.objects.values('key').filter(key=key)

    for notification_type in notification_type_ids:
        channel_layer.group_send(
            settings.NOTIFICATION_CHANNEL.format(
                notification_key=notification_type['key']
            ),
            {'text': 'new-notification'}
        )

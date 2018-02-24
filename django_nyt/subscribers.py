import logging

from channels import Group

from . import models, settings

logger = logging.getLogger(__name__)


def notify_subscribers(notifications, key):
    """
    Notify all open channels about new notifications
    """

    logger.debug("Broadcasting to subscribers")

    notification_type_ids = models.NotificationType.objects.values('key').filter(key=key)

    for notification_type in notification_type_ids:
        g = Group(
            settings.NOTIFICATION_CHANNEL.format(
                notification_key=notification_type['key']
            )
        )
        g.send(
            {'text': 'new-notification'}
        )

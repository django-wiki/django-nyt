import logging

from channels.consumer import SyncConsumer


from . import models, settings

logger = logging.getLogger(__name__)


class NytConsumer(SyncConsumer):

    def get_subscriptions(self):
        """
        :return: Subscription query for a given message's user
        """
        user = self.scope['user']
        if user and user.is_authenticated:
            return models.Subscription.objects.filter(settings__user=user)
        else:
            return models.Subscription.objects.none()

    def websocket_connect(self, event):
        """
        Connected to websocket.connect
        """
        logger.debug("Adding new connection for user {}".format(self.scope['user']))
        self.send({"type": "websocket.accept"})

        for subscription in self.get_subscriptions():
            self.channel_layer.group_add(
                settings.NOTIFICATION_CHANNEL.format(
                    notification_key=subscription.notification_type.key
                ), self.channel_name
            )

    def websocket_disconnect(self, event):
        """
        Connected to websocket.disconnect
        """
        logger.debug("Removing connection for user {} (disconnect)".format(self.scope['user']))
        for subscription in self.get_subscriptions():
            self.channel_layer.group_discard(
                settings.NOTIFICATION_CHANNEL.format(
                    notification_key=subscription.notification_type.key
                ), self.channel_name
            )

    def websocket_receive(self, event):
        """
        Receives messages, this is currently just for debugging purposes as there
        is no communication API for the websockets.
        """
        logger.debug("Received a message, responding with a non-API message")
        self.send({"type": "websocket.send", 'text': event['text']})


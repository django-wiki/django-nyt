from logging import getLogger

from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async

from . import models, settings

logger = getLogger(name=__name__)


class NytConsumer(AsyncConsumer):

    @database_sync_to_async
    def get_subscriptions(self):
        """
        :return: Subscription query for a given message's user
        """
        user = self.scope['user']
        if user and user.is_authenticated:
            return models.Subscription.objects.filter(settings__user=user)

        else:
            return models.Subscription.objects.none()

    @database_sync_to_async
    def presence_out(self):
        user = self.scope['user']
        if hasattr(user, 'update_presence'):
            user.update_presence(False)

    @database_sync_to_async
    def presence_in(self):
        user = self.scope['user']
        if hasattr(user, 'update_presence'):
            user.update_presence(True)

    async def websocket_connect(self, event):
        """
        Connected to websocket.connect
        """
        logger.debug("Adding new connection for user {}".format(self.scope['user']))
        await self.send({"type": "websocket.accept"})
        subscriptions = await self.get_subscriptions()
        for subscription in subscriptions:
            await self.channel_layer.group_add(
                settings.NOTIFICATION_CHANNEL.format(
                    notification_key=subscription.notification_type.key
                ), self.channel_name
            )
        await self.presence_in()

    async def wsconnect(self, event):
        """
        Connected to wsconnect
        """
        logger.debug("Adding new connection for user {}".format(self.scope['user']))
        await self.send({"type": "websocket.accept"})
        subscriptions = await self.get_subscriptions()
        for subscription in subscriptions:
            await self.channel_layer.group_add(
                settings.NOTIFICATION_CHANNEL.format(
                    notification_key=subscription.notification_type.key
                ), self.channel_name
            )
        await self.presence_in()

    async def websocket_disconnect(self, event):
        """
        Connected to websocket.disconnect
        """
        logger.debug("Removing connection for user {} (disconnect)".format(self.scope['user']))
        subscriptions = await self.get_subscriptions()
        for subscription in subscriptions:
            await self.channel_layer.group_discard(
                settings.NOTIFICATION_CHANNEL.format(
                    notification_key=subscription.notification_type.key
                ), self.channel_name
            )
        await self.presence_out()

    async def wsdisconnect(self, event):
        """
        Connected to wsdisconnect
        """
        logger.debug("Removing connection for user {} (disconnect)".format(self.scope['user']))
        subscriptions = await self.get_subscriptions()
        for subscription in subscriptions:
            await self.channel_layer.group_discard(
                settings.NOTIFICATION_CHANNEL.format(
                    notification_key=subscription.notification_type.key
                ), self.channel_name
            )
        await self.presence_out()

    async def websocket_receive(self, event):
        """
        Receives messages, this is currently just for debugging purposes as there
        is no communication API for the websockets.
        """
        logger.debug("Received a message, responding with a non-API message")
        await self.send({"type": "websocket.send", 'text': event['text']})

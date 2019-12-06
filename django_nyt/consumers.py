from logging import getLogger

from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
import json
import six
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
        await self.presence_in()
        await self.send({"type": "websocket.accept"})

        subscriptions = await self.get_subscriptions()
        for subscription in subscriptions:
            await self.channel_layer.group_add(
                settings.NOTIFICATION_CHANNEL.format(
                    notification_key=subscription.notification_type.key
                ), self.channel_name
            )

        await self.channel_layer.group_add(
            'nyt_personal-{}'.format(self.scope['user'].api_uuid), self.channel_name
        )

    async def wsconnect(self, event):
        """
        Connected to wsconnect
        """
        await self.websocket_connect(event)

    async def websocket_disconnect(self, event):
        """
        Connected to websocket.disconnect
        """
        logger.debug("Removing connection for user {} (disconnect)".format(self.scope['user']))
        await self.presence_out()
        subscriptions = await self.get_subscriptions()
        for subscription in subscriptions:
            await self.channel_layer.group_discard(
                settings.NOTIFICATION_CHANNEL.format(
                    notification_key=subscription.notification_type.key
                ), self.channel_name
            )

        await self.channel_layer.group_discard(
            'nyt_personal-{}'.format(self.scope['user'].api_uuid), self.channel_name
        )

    async def wsdisconnect(self, event):
        """
        Connected to wsdisconnect
        """
        await self.websocket_disconnect(event)

    async def websocket_subscribe(self, event):
        logger.debug("Adding new subscription on channel layer for user {}".format(self.scope['user']))

        await self.channel_layer.group_add(
            event['room'], self.channel_name
        )

    async def websocket_receive(self, event):
        await self.send(self.event_to_msg(event))

    async def websocket_send(self, event):
        await self.send(self.event_to_msg(event))

    def event_to_msg(self, event):
        if event.get('text'):
            return {"type": "websocket.send", 'text': self.parse_event_text(event['text'])}
        return {"type": "websocket.send", 'text': 'empty message'}

    @staticmethod
    def parse_event_text(text):
        if not isinstance(text, six.string_types):
            return json.dumps(text)
        return text

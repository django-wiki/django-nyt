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

    @database_sync_to_async
    def room_members_online(self, roomName):
        user = self.scope['user']
        queryset = user._meta.model.medics.online().filter(nyt_settings__subscription__notification_type__key=roomName)
        return queryset.count()

    async def websocket_connect(self, event):
        """
        Connected to websocket.connect
        """
        logger.debug("Adding new connection for user {}".format(self.scope['user']))
        await self.presence_in()
        await self.send({"type": "websocket.accept"})

        subscriptions = await self.get_subscriptions()
        for subscription in subscriptions:
            channel = settings.NOTIFICATION_CHANNEL.format(
                    notification_key=subscription.notification_type.key)
            await self.channel_layer.group_add(channel, self.channel_name)

        await self.channel_layer.group_add(
            'nyt_personal-{}'.format(self.scope['user'].api_uuid), self.channel_name
        )

    async def websocket_subscribe(self, event):
        logger.debug("Adding new subscription on channel layer for user {}".format(self.scope['user']))

        await self.channel_layer.group_add(
            event['room'], self.channel_name
        )
        
    async def wsconnect(self, event):
        """
        Connected to wsconnect
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

        self.channel_layer.group_add(
            'nyt_personal-{}'.format(self.scope['user'].api_uuid)
        )

    async def websocket_disconnect(self, event):
        """
        Connected to websocket.disconnect
        """
        logger.debug("Removing connection for user {} (disconnect)".format(self.scope['user']))
        subscriptions = await self.get_subscriptions()
        await self.presence_out()
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
        from . import utils
        """
        Receives messages, this is currently just for debugging purposes as there
        is no communication API for the websockets.
        """
        logger.debug("Received a message, responding with a non-API message")
        if event.get('text'):
            data = utils.parse_event(event, self.scope['user'])
            room = data.get('room')
            message = data.get('message')
            sender = data.get('sender', str(self.scope['user'].api_uuid))
            if room:
                channel_name = settings.NOTIFICATION_CHANNEL.format(notification_key=room)
                if data.get('event') == 'subscribe':
                    self.channel_layer.group_add(channel_name, self.channel_name)
                    await self.channel_layer.group_send(channel_name, {'type': 'webrtc.members', 'room': room})
                elif message:
                    await self.channel_layer.group_send(
                        channel_name,
                        {"type": "webrtc.send", 'text': message, 'sender': sender}
                    )
            else:
                msg = {"type": "websocket.send", 'text': event['text']}
                await self.send(msg)

    async def webrtc_send(self, event):
        msg = {"type": "websocket.send", 'text': event['text']}
        
        if not isinstance(msg['text'], six.string_types):
            msg['text'] = json.dumps(msg['text'])
        
        if event['sender'] != str(self.scope['user'].api_uuid):
            await self.send(msg)

    async def webrtc_members(self, event):
        members = await self.room_members_online(event['room'])
        if members > 1:
            msg = {"type": "websocket.send", 'text': json.dumps({'members': members})}
            await self.send(msg)
            

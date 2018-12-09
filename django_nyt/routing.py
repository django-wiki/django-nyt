from django.urls import path
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from . import consumers


main_router = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('nyt', consumers.NytConsumer),
        ])
    )
})

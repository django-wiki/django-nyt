from django.conf.urls import url
from channels.routing import URLRouter
from channels.auth import AuthMiddlewareStack

from . import consumers

channel_routing = AuthMiddlewareStack(
    URLRouter([
        url(r"^nyt/$", consumers.NytConsumer),
    ])
)

# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import logging

from channels import Group

from . import settings

logger = logging.getLogger(__name__)


# Connected to websocket.connect
def ws_connect(message):
    logger.debug("Adding new connection")
    Group(settings.NOTIFICATION_CHANNEL).add(message.reply_channel)

# Connected to websocket.disconnect
def ws_disconnect(message):
    logger.debug("Removing connection (disconnect)")
    Group(settings.NOTIFICATION_CHANNEL).discard(message.reply_channel)

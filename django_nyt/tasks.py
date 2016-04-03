# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import logging

from channels import Group

from . import settings

logger = logging.getLogger(__name__)


def notify_subscribers(notifications):
    """
    Notify all open channels about new notifications
    """

    logger.debug("Broadcasting to subscribers")

    g = Group(settings.NOTIFICATION_CHANNEL)
    g.send(
        {'event': 'new-notification'}
    )

    print g.channel_layer._groups

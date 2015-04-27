# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

_disable_notifications = False

VERSION = "0.9.7.2"


def notify(*args, **kwargs):
    """
    DEPRECATED - please access django_nyt.utils.notify
    """
    from django_nyt.utils import notify
    return notify(*args, **kwargs)

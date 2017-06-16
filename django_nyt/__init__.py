# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

_disable_notifications = False

VERSION = "1.0b5"
__version__ = VERSION


def notify(*args, **kwargs):
    """
    DEPRECATED - please access django_nyt.utils.notify
    """
    from django_nyt.utils import notify
    return notify(*args, **kwargs)

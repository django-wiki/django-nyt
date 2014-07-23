# -*- coding: utf-8 -*-
_disable_notifications = False

VERSION = "0.9.3"


def notify(*args, **kwargs):
    """
    DEPRECATED - please access django_nyt.utils.notify
    """
    from django_nyt.utils import notify
    return notify(*args, **kwargs)

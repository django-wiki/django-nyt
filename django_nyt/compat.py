# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import django

def is_authenticated(user):
    if django.VERSION >= (1, 10):
        is_authenticated = user.is_authenticated
    else:
        is_authenticated = user.is_authenticated()
    return is_authenticated

# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import json

from functools import wraps

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

import django_nyt


def disable_notify(f):
    """Disable notifications. Example:

    @disable_notify
    def your_function():
        notify("no one will be notified", ...)
    """
    @wraps(f)
    def wrapper(request, *args, **kwargs):
        django_nyt._disable_notifications = True
        response = f(request, *args, **kwargs)
        django_nyt._disable_notifications = False
        return response
    return wrapper


def login_required_ajax(f):
    """Similar to login_required. But if the request is an ajax request, then
    it returns an error in json with a 403 status code."""

    @wraps(f)
    def wrapper(request, *args, **kwargs):
        if request.is_ajax():
            if not request.user or not request.user.is_authenticated():
                return json_view(lambda *a,
                                 **kw: {'error': 'not logged in'})(request,
                                                                   status=403)
            return f(request, *args, **kwargs)
        else:
            return login_required(f)(request, *args, **kwargs)
    return wrapper


def data2jsonresponse(data, **kwargs):
    json_data = json.dumps(data, ensure_ascii=False)
    status = kwargs.get('status', 200)
    response = HttpResponse(content_type='application/json', status=status)
    response.write(json_data)
    return response


def json_view(f):
    @wraps(f)
    def wrapper(request, *args, **kwargs):
        data = f(request, *args, **kwargs)
        return data2jsonresponse(data, **kwargs)
    return wrapper

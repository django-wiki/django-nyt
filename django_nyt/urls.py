# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from django import VERSION as DJANGO_VERSION
from django.conf.urls import url, include

from . import views

app_name = 'nyt'

urlpatterns = [
    url('^json/get/$', views.get_notifications, name='json_get'),
    url('^json/get/(?P<latest_id>\d+)/$', views.get_notifications, name='json_get'),
    url('^json/mark-read/$', views.mark_read, name='json_mark_read_base'),
    url('^json/mark-read/(\d+)/$', views.mark_read, name='json_mark_read'),
    url('^json/mark-read/(?P<id_lte>\d+)/(?P<id_gte>\d+)/$', views.mark_read, name='json_mark_read'),
    url('^goto/(?P<notification_id>\d+)/$', views.goto, name='goto'),
    url('^goto/$', views.goto, name='goto_base'),
]


if DJANGO_VERSION < (1, 8):
    from django.conf.urls import patterns  # noqa @UnresolvedImport
    urlpatterns = patterns('', *urlpatterns)


def get_pattern(app_name=app_name, namespace="nyt"):
    """Every url resolution takes place as "nyt:view_name".
       https://docs.djangoproject.com/en/dev/topics/http/urls/#topics-http-reversing-url-namespaces
    """
    if DJANGO_VERSION < (1, 9):
        return urlpatterns, app_name, namespace
    else:
        return include('django_nyt.urls',)

# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from django import VERSION as DJANGO_VERSION
from django.conf.urls import url

urlpatterns = [
    url('^json/get/$', 'django_nyt.views.get_notifications', name='json_get'),
    url('^json/get/(?P<latest_id>\d+)/$', 'django_nyt.views.get_notifications', name='json_get'),
    url('^json/mark-read/$', 'django_nyt.views.mark_read', name='json_mark_read_base'),
    url('^json/mark-read/(\d+)/$', 'django_nyt.views.mark_read', name='json_mark_read'),
    url('^json/mark-read/(?P<id_lte>\d+)/(?P<id_gte>\d+)/$', 'django_nyt.views.mark_read', name='json_mark_read'),
    url('^goto/(?P<notification_id>\d+)/$', 'django_nyt.views.goto', name='goto'),
    url('^goto/$', 'django_nyt.views.goto', name='goto_base'),
]


if DJANGO_VERSION < (1, 8):
    from django.conf.urls import patterns
    urlpatterns = patterns('', *urlpatterns)


def get_pattern(app_name="nyt", namespace="nyt"):
    """Every url resolution takes place as "nyt:view_name".
       https://docs.djangoproject.com/en/dev/topics/http/urls/#topics-http-reversing-url-namespaces
    """
    return urlpatterns, app_name, namespace

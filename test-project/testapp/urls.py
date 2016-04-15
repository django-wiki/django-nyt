# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from django.conf.urls import url

from . import views

app_name = 'testapp'


urlpatterns = [
    url(r'^$', views.TestIndex.as_view(), name='index'),
    url(r'^create/$', views.CreateTestModelView.as_view(), name='create'),
    url(r'^login-as/(?P<pk>\d+)/$', views.TestLoginAsUser.as_view(), name='login_as'),
]

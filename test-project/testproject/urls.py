from __future__ import absolute_import
from __future__ import unicode_literals

import django.views.static

from django import VERSION as DJANGO_VERSION
from django.conf.urls import include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin


admin.autodiscover()

urlpatterns = [
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('testapp.urls')),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', django.views.static.serve, kwargs={
            'document_root': settings.MEDIA_ROOT,
        }),
    ]


from django_nyt.urls import get_pattern

urlpatterns += [
    url(r'^nyt/', get_pattern()),
]

if DJANGO_VERSION < (1, 8):
    from django.conf.urls import patterns
    urlpatterns = patterns('', *urlpatterns)

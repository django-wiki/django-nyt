import django.views.static
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

try:
    from django.urls import include, re_path as url
except ImportError:
    from django.conf.urls import include, url


admin.autodiscover()

urlpatterns = [
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^nyt/', include('django_nyt.urls')),
    url(r'', include('testapp.urls')),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', django.views.static.serve, kwargs={
            'document_root': settings.MEDIA_ROOT,
        }),
    ]

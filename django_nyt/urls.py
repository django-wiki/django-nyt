from django.conf.urls import include
from django.conf.urls import url

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


def get_pattern(app_name=app_name, namespace="nyt"):
    """Every url resolution takes place as "nyt:view_name".
       https://docs.djangoproject.com/en/dev/topics/http/urls/#topics-http-reversing-url-namespaces
    """
    import warnings
    warnings.warn(
        'django_nyt.urls.get_pattern is deprecated and will be removed in next version,'
        ' just use include(\'django_nyt.urls\')', DeprecationWarning
    )
    return include('django_nyt.urls')

from django.urls import include, re_path as url

from . import views

app_name = 'nyt'

urlpatterns = [
    url(r'^json/get/$', views.get_notifications, name='json_get'),
    url(r'^json/get/(?P<latest_id>\d+)/$', views.get_notifications, name='json_get'),
    url(r'^json/mark-read/$', views.mark_read, name='json_mark_read_base'),
    url(r'^json/mark-read/(\d+)/$', views.mark_read, name='json_mark_read'),
    url(r'^json/mark-read/(?P<id_lte>\d+)/(?P<id_gte>\d+)/$', views.mark_read, name='json_mark_read'),
    url(r'^goto/(?P<notification_id>\d+)/$', views.goto, name='goto'),
    url(r'^goto/$', views.goto, name='goto_base'),
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

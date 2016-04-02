from django.conf.urls import url

from . import views

app_name = 'testapp'


urlpatterns = [
    url(r'^$', views.TestIndex.as_view(), name='index'),
    url(r'^login-as/(?P<pk>\d+)/$', views.TestLoginAsUser.as_view(), name='login_as'),
]

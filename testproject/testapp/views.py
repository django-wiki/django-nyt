from __future__ import absolute_import
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from django_nyt.models import Notification, Settings

from . import models
from django_nyt.forms import SettingsForm


class TestIndex(CreateView):

    model = models.TestModel
    fields = ('name',)
    template_name = "testapp/index.html"

    def get_context_data(self, **kwargs):
        c = CreateView.get_context_data(self, **kwargs)
        user_model = get_user_model()
        c['users'] = user_model.objects.all()
        if self.request.user.is_authenticated():
            c['notifications'] = Notification.objects.filter(
                user=self.request.user
            ).order_by(
                '-created'
            )
            c['settings_form'] = SettingsForm(
                instance=Settings.get_default_setting(self.request.user)
            )
        return c

    def form_valid(self, form):
        # There is a signal on TestModel that will create notifications
        form.save()
        return redirect('testapp:index')


class TestLoginAsUser(DetailView):

    model = get_user_model()

    def get(self, *args, **kwargs):
        user = self.get_object()
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(self.request, user)
        return redirect('testapp:index')

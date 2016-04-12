from __future__ import absolute_import
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from django_nyt.forms import SettingsForm
from django_nyt.models import Notification, Settings
from django_nyt.decorators import json_view

from . import forms
from . import models

from django.utils.decorators import method_decorator


class TestIndex(TemplateView):

    template_name = "testapp/index.html"

    def get_context_data(self, **kwargs):
        c = TemplateView.get_context_data(self, **kwargs)
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
            c['testmodel_form'] = forms.TestModelForm()
        return c


class CreateTestModelView(CreateView):
    model = models.TestModel
    form_class = forms.TestModelForm

    @method_decorator(json_view)
    def dispatch(self, request, *args, **kwargs):
        return CreateView.dispatch(self, request, *args, **kwargs)

    def form_valid(self, form):
        # There is a signal on TestModel that will create notifications
        form.save()
        return {
            'OK': True
        }

    def form_invalid(self, form):
        return {
            'OK': False
        }


class TestLoginAsUser(DetailView):

    model = get_user_model()

    def get(self, *args, **kwargs):
        user = self.get_object()
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(self.request, user)
        return redirect('testapp:index')

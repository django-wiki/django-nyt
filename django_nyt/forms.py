# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from django import forms

from . import models


class SettingsForm(forms.ModelForm):

    class Meta:
        model = models.Settings
        fields = (
            'interval',
            'is_default',
        )

from django import forms

from . import models


class SettingsForm(forms.ModelForm):

    class Meta:
        model = models.Settings
        fields = (
            'interval',
            'is_default',
        )

from django import forms

from . import models

class TestModelForm(forms.ModelForm):

    class Meta:
        model = models.TestModel
        fields = ('name',)

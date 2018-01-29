from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class DjangoNytConfig(AppConfig):
    name = "django_nyt"
    verbose_name = _("Django Nyt")

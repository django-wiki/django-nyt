from django.conf import settings as django_settings

from . import defaults


def __getattr__(name):
    """
    The attribute getter for this module makes it possible to
    lazily/dynamically access the settings defined in django_nyt.settings.defaults.
    """

    # All attributes accessed with this prefix are possible to overwrite
    # through django.conf.settings.
    settings_prefix = "NYT_"

    if name in defaults.__dict__.keys():

        default = getattr(defaults, name)
        if name.startswith(settings_prefix):
            return getattr(django_settings, name, default)
        return default

    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

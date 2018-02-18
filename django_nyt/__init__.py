_disable_notifications = False

VERSION = "1.0"
__version__ = VERSION

default_app_config = "django_nyt.apps.DjangoNytConfig"


def notify(*args, **kwargs):
    """
    DEPRECATED - please access django_nyt.utils.notify
    """
    from django_nyt.utils import notify
    return notify(*args, **kwargs)

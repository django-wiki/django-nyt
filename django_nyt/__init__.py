_disable_notifications = False

__version__ = "1.1"

default_app_config = "django_nyt.apps.DjangoNytConfig"


def notify(*args, **kwargs):
    """
    DEPRECATED - please access django_nyt.utils.notify
    """
    from django_nyt.utils import notify
    return notify(*args, **kwargs)

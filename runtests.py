#!/usr/bin/env python
import sys
import django
from django import VERSION
from django.conf import settings

INSTALLED_APPS=[
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.humanize',
    'django.contrib.sites',
    'django_nyt',
]


if VERSION < (1, 7):
    INSTALLED_APPS.append('south')

settings.configure(
    DEBUG=True,
#    AUTH_USER_MODEL='testdata.CustomUser',
    DATABASES={
         'default': {
             'ENGINE': 'django.db.backends.sqlite3',
         }
    },
    SITE_ID=1,
    ROOT_URLCONF='testproject.urls',
    INSTALLED_APPS=INSTALLED_APPS,
    TEMPLATE_CONTEXT_PROCESSORS=(
        "django.contrib.auth.context_processors.auth",
        "django.core.context_processors.debug",
        "django.core.context_processors.i18n",
        "django.core.context_processors.media",
        "django.core.context_processors.request",
        "django.core.context_processors.static",
        "django.core.context_processors.tz",
        "django.contrib.messages.context_processors.messages",
    ),
    USE_TZ=True,
    SOUTH_TESTS_MIGRATE=True,
)


# If you use South for migrations, uncomment this to monkeypatch
# syncdb to get migrations to run.
if VERSION < (1, 7):
    from south.management.commands import patch_for_test_db_setup
    patch_for_test_db_setup()

from django.core.management import execute_from_command_line
argv = [sys.argv[0], "test"]

if len(sys.argv) == 1:
    # Nothing following 'runtests.py':
    if django.VERSION < (1,6):
        argv.append("django_nyt")
    else:
        argv.append("django_nyt.tests")
else:
    # Allow tests to be specified:
    argv.extend(sys.argv[1:])

execute_from_command_line(argv)

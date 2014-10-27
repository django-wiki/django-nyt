#!/usr/bin/env python
import sys
import django
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


from django import VERSION
if VERSION <= (1, 6):
    INSTALLED_APPS.append('south')
    SOUTH_MIGRATION_MODULES = {
        'django_nyt': 'django_nyt.south_migrations',
    }
else:
    TEST_RUNNER = 'django.test.runner.DiscoverRunner'

from django import VERSION
if VERSION <= (1, 6):
    INSTALLED_APPS.append('south')
    SOUTH_MIGRATION_MODULES = {
        'django_nyt': 'django_nyt.south_migrations',
    }
#    TEST_RUNNER = None
else:
    SOUTH_MIGRATION_MODULES = None
#    TEST_RUNNER = 'django.test.runner.DiscoverRunner'

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
    SOUTH_MIGRATION_MODULES=SOUTH_MIGRATION_MODULES,
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

#!/usr/bin/env python
import os
import sys
from django.conf import settings

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.humanize',
    'django.contrib.sites',
    'django_nyt',
    'testapp',
]


settings.configure(
    DEBUG=True,
    # AUTH_USER_MODEL='testdata.CustomUser',
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
    MIDDLEWARE_CLASSES=[
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    ],
)


from django.core.management import execute_from_command_line
argv = [sys.argv[0], "test"]

if len(sys.argv) == 1:
    argv.append("django_nyt.tests")
else:
    # Allow tests to be specified:
    argv.extend(sys.argv[1:])

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'test-project'))
execute_from_command_line(argv)

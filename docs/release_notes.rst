Release Notes
=============

1.4 (unreleased)
----------------

* Tests migrated to pytest #123 (Benjamin Balder Bach)


1.3
---

* Hatch build system, environment management and more #116 (Oscar Cortez)
* pre-commit configuration updated #116 (Oscar Cortez)
* Code-base black'ned #116 (Oscar Cortez)


1.2.4
-----

* Adds Django 4.1 support #113 (Oscar Cortez)


1.2.3
-----

* Add missing .txt email template files in distributed packages #109


1.2.2
-----

* Adds a no-op migration because of auto-detected changes


1.2.1
-----

* Django 4.0 and Python 3.10 support (added to test matrix)


1.2
---

Added
^^^^^

* Django 3.2 and Python 3.9 support (added to test matrix)
* Travis replaced with Circle CI

Removed
^^^^^^^

* Django 1.11 and 2.1 support


1.1.6
-----

Added
^^^^^

* Django 3.1 support (added to test matrix)

1.1.5
-----

Fixed
^^^^^

* Do not access ``Settings.user`` in ``Settings.clean()`` on blank new objects :url-pr:`92`


1.1.4
-----

Added
^^^^^

* Django 3.0 support (added to test matrix)


1.1.3
-----

Added
^^^^^

* Django 2.2 support (added to test matrix)
* Linting (no changes to functionality)


1.1.2
-----

Added
^^^^^

* Django 2.1 support (no changes in code)


1.1.1
-----

Added
^^^^^

* Python 3.7 support  :url-pr:`81`

Deprecations
^^^^^^^^^^^^

* Removed ``django_nyt.notify``, use ``django_nyt.utils.notify``



1.1
---

New features
^^^^^^^^^^^^

* Django 2.0 support :url-pr:`55`

Bug fixes
^^^^^^^^^

* Restored missing translation files :url-pr:`73`

Deprecations
^^^^^^^^^^^^

* Django < 1.11 support is dropped :url-pr:`62`
* Python < 3.4 support is dropped :url-pr:`65` and :url-pr:`68`
* Deprecate ``django_nyt.urls.get_pattern``, use ``include('django_nyt.urls')`` instead :url-pr:`63`
* Removed ``django_nyt.VERSION``, use `django_nyt.__version__` instead :url-pr:`73`

1.0
---

Starting from django-nyt 1.0, support for the upcoming
`channels <https://channels.readthedocs.io/en/stable/>`_ has been added together with
Django 1.9, 1.10 and 1.11 support.

You can switch off django-channels by setting
``settings.NYT_CHANNELS_DISABLE = True``.


New features
^^^^^^^^^^^^

* Support for ``channels`` and web sockets. :url-pr:`21`
* Django 1.9, 1.10, and 1.11 support :url-pr:`25`
* Default AppConfig ``"django_nyt.apps.DjangoNytConfig"`` :url-pr:`57`


Bug fixes
^^^^^^^^^

* Celery will auto-load ``django_nyt.tasks`` when ``channels`` isn't installed :url-issue:`23`
* Error in channels consumer when requested with AnonymousUser (Benjamin Bach) :url-issue:`50` :url-pr:`51`
* Clear the notification type cache every time a new notification type is created or deleted (Benjamin Bach) :url-issue:`34` :url-pr:`36`
* Explicitly accept WebSocket connections (Kim Desrosiers) :url-pr:`35`
* Fix critical django-channels err (Tomaž Žniderič) :url-issue:`29`
* Correctly set default options for ``notifymail`` management command (Benjamin Bach) :url-pr:`32`
* Adds Django 1.11 to test matrix (Benjamin Bach) :url-pr:`32`
* Do not return ``bytes`` in ``__str__`` (Øystein Hiåsen) :url-pr:`28`


Deprecations
^^^^^^^^^^^^

* Django 1.5 and 1.6 support is dropped

Release Notes
=============

1.1.6
-----

Added
^^^^^

* Django 3.1 support (added to test matrix)

1.1.5
-----

Fixed
^^^^^

* Do not access ``Settings.user`` in ``Settings.clean()`` on blank new objects :url-issue:`92`


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

* Python 3.7 support  :url-issue:`81`

Deprecations
^^^^^^^^^^^^

* Removed ``django_nyt.notify``, use ``django_nyt.utils.notify``



1.1
---

New features
^^^^^^^^^^^^

* Django 2.0 support :url-issue:`55`

Bug fixes
^^^^^^^^^

* Restored missing translation files :url-issue:`73`

Deprecations
^^^^^^^^^^^^

* Django < 1.11 support is dropped :url-issue:`62`
* Python < 3.4 support is dropped :url-issue:`65` and :url-issue:`68`
* Deprecate ``django_nyt.urls.get_pattern``, use ``include('django_nyt.urls')`` instead :url-issue:`63`
* Removed ``django_nyt.VERSION``, use `django_nyt.__version__` instead :url-issue:`73`

1.0
---

Starting from django-nyt 1.0, support for the upcoming
`channels <http://channels.readthedocs.io/>`_ has been added together with
Django 1.9, 1.10 and 1.11 support.

You can switch off django-channels by setting
``settings.NYT_CHANNELS_DISABLE = True``.


New features
^^^^^^^^^^^^

* Support for ``channels`` and web sockets. :url-issue:`21`
* Django 1.9, 1.10, and 1.11 support :url-issue:`25`
* Default AppConfig ``"django_nyt.apps.DjangoNytConfig"`` :url-issue:`57`


Bug fixes
^^^^^^^^^

* Celery will auto-load ``django_nyt.tasks`` when ``channels`` isn't installed :url-issue:`23`
* Error in channels consumer when requested with AnonymousUser (Benjamin Bach) :url-issue:`50` :url-issue:`51`
* Clear the notification type cache every time a new notification type is created or deleted (Benjamin Bach) :url-issue:`34` :url-issue:`36`
* Explicitly accept WebSocket connections (Kim Desrosiers) :url-issue:`35`
* Fix critical django-channels err (Tomaž Žniderič) :url-issue:`29`
* Correctly set default options for ``notifymail`` management command (Benjamin Bach) :url-issue:`32`
* Adds Django 1.11 to test matrix (Benjamin Bach) :url-issue:`32`
* Do not return ``bytes`` in ``__str__`` (Øystein Hiåsen) :url-issue:`28`


Deprecations
^^^^^^^^^^^^

* Django 1.5 and 1.6 support is dropped

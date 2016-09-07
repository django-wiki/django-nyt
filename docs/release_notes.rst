Release Notes
=============

1.0b1
-----

Starting from django-nyt 1.0, support for the upcoming
`channels <http://channels.readthedocs.io/>`_ has been added together with
Django 1.9 support.

You can switch off django-channels by setting
``settings.NYT_CHANNELS_DISABLE = True``.


New features
^^^^^^^^^^^^

 * Support for ``channels`` and web sockets. :url-issue:`21`
 * Django 1.9 and 1.10 support :url-issue:`25`


Bug fixes
^^^^^^^^^

 * Celery will auto-load ``django_nyt.tasks`` when ``channels`` isn't installed :url-issue:`23`


Deprecations
^^^^^^^^^^^^

 * Django 1.5 and 1.6 support is dropped

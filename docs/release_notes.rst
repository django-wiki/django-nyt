Release Notes
=============

1.1
---

New features
^^^^^^^^^^^^

 * ...

Bug fixes
^^^^^^^^^

 * ...

Deprecations
^^^^^^^^^^^^

 * ...

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

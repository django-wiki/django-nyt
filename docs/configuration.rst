Configuration
=============

Refer to ``django_nyt.settings`` for full details of available configuration.

NYT_ENABLED
~~~~~~~~~~~

 * Default: True

You can completely turn off notifications by setting this to False.

NYT_ENABLE_ADMIN
~~~~~~~~~~~~~~~~

 * Default: False

Enables django-admin ModelAdmin for django_nyt models.

NYT_SEND_EMAILS
~~~~~~~~~~~~~~~

 * Default: True

You can disable emails with this setting. Emails are sent with `python manage.py notifymail`

NYT_EMAIL_SUBJECT
~~~~~~~~~~~~~~~~~

 * Default: _("You have new notifications")

NYT_EMAIL_SENDER
~~~~~~~~~~~~~~~~

 * Default: "notifications@example.com"

NYT_INTERVALS
~~~~~~~~~~~~~

 * Default:

.. code-block:: python

   [
       (INSTANTLY, _(u'instantly')),
       (DAILY, _(u'daily')),
       (WEEKLY, _(u'weekly')),
   ]


NYT_PID
~~~~~~~

 * Default: ``/tmp/nyt_daemon.pid``

The PID of currently running daemon is stored here. By running ``python manage.py notifymail --daemon``, you get a daemon that sends mail periodically.


NYT_LOG
~~~~~~~

 * Default: ``/tmp/nyt_daemon.log``

Logging of email sending.


Planned settings
================

The following settings should become operatable somehow someday. Please implement them at will :)

NYT_AUTO_DELETE
~~~~~~~~~~~~~~~

 * Default: 120

After how many days should viewed notifications be deleted?

NYT_AUTO_DELETE_ALL
~~~~~~~~~~~~~~~~~~~

 * Default: 120

After how many days should all types of notifications be deleted?

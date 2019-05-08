django-nyt
==========

.. image:: https://travis-ci.org/django-wiki/django-nyt.png?branch=master
   :target: https://travis-ci.org/django-wiki/django-nyt
.. image:: https://readthedocs.org/projects/django-nyt/badge/?version=latest
   :target: http://django-nyt.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status
.. image:: https://badge.fury.io/py/django-nyt.svg
   :target: https://pypi.python.org/pypi/django-nyt
.. image:: http://codecov.io/github/django-wiki/django-nyt/coverage.svg?branch=master
  :target: http://codecov.io/github/django-wiki/django-nyt?branch=master

What the fork
-------------
It's a fork migrated to channels-2 and pure async code
Also, added presence trigger to user model.
For using presence you need add method to your UserModel like
.. code:: python

    def update_presence(self, presence):
        UserPresence.objects.update_or_create(
            defaults={'user': self, 'status': presence or False}
        )

    class UserPresence(models.Model):
        user = models.OneToOneField('custom_app.UserCustomModel',
                                    related_name='presence',
                                    on_delete=models.CASCADE)
        status = models.BooleanField(default=False)
        last_updated = models.DateTimeField(auto_now=True, editable=False)

        class Meta:
            verbose_name = _('user presence')
            verbose_name_plural = _("user presences")

        def __str__(self):
            status = _('Online') if self.status else _('Offline')
            return f'{status} on {self.last_updated}'

`custom_app.UserCustomModel` replace to your user model or use django's default

Concept
-------

django-nyt is a notification framework for Django, it does this:

.. code:: python

    from django_nyt.utils import notify

    EVENT_KEY = "my_key"
    notify(_("OMG! Something happened"), EVENT_KEY)

All users subscribing to ``"my_key"`` will have a notification created
in their stack when ``notify()`` is called.

If you have emails enabled, subscribers receive a summary of notifications at
an interval of their choice.

Data can be accessed easily from Django models or from the included JSON
views.

Channels (django-channels) UPD in 1.2.0
--------------------------

Starting from django-nyt 1.2.0, working on
`channels-2 <https://channels.readthedocs.io/en/latest/>`_
together with Django 2.1+



Docs
----

http://django-nyt.readthedocs.io/en/latest/


Why should you do this?
-----------------------

Users need a cleverly sifted stream of events that's highly customizable
as well. By using django-nyt, your users can subscribe to global events
or specific events pertaining specific objects.

Instead of inventing your own notification system, use this and you won't have
to design your own models, and you will have a nice guide that goes through
the various steps of implementing notifications for your project.

Let's try to summarize the reasons you want to be using django-nyt:

 - Simple API: call ``notify()`` where-ever you want.
 - CLI for sending emails (as cron job, daemon or Celery task)
 - Support for django-channels and Web Sockets (optional, fallback for JSON-based polling)
 - Basic JavaScript / HTML example code
 - Multi-lingual
 - Individual subscription settings for each type of event, for instance:
   - Event type A spawns instant email notifications, but Event B only gets emailed weekly.
 - Customizable intervals for which users can receive notifications
 - Optional URL for action target for each notification
 - Avoid clutter: Notifications don't get repeated, instead a counter is incremented.

This project exists with ``django.contrib.messages`` in mind, to serve a simple,
best-practice, scalable solution for notifications. There are loads of other
notification apps for Django, some focus on integration of specific communication
protocols

What do you need to do?
-----------------------

django-nyt does everything it can to meet as many needs as possible and
have sane defaults.

But you need to do a lot! Firstly, you need to write some JavaScript that will
fetch the latest notifications and display them in some area of the
screen. Upon clicking that icon, the latest notifications are displayed, and
clicking an individual notification will redirect the user through a page
that marks the notification as read.

Something like this:

.. image:: https://raw.githubusercontent.com/django-wiki/django-nyt/master/docs/misc/screenshot_dropdown.png
   :alt: Javascript drop-down

JavaScript drop-down: Some examples are provided in the docs, but there
is no real easy way to place this nifty little thing at the top of your
site, you're going to have to work it out on your own.

Other items for your TODO list:

-  Provide your users with options to customize their subscriptions and
   notification preferences. Create your own ``Form`` inheriting from
   ``django_nyt.forms.SettingsForm``.
-  Customize contents of notification emails by overwriting templates in
   ``django_nyt/emails/notification_email_message.txt`` and
   ``django_nyt/emails/notification_email_subject.txt``.
-  Make the mail notification daemon script run either constantly
   ``python manage.py notifymail --daemon`` or with some interval by invoking
   ``python manage.py notifymail --cron`` as a cronjob. You can also call it
   from a Celery task or similar with ``call_command('notifymail', cron=True)``.


Development / demo project
--------------------------

In your Git fork, run ``pip install -r requirements.txt`` to install the
requirements.

Install pre-commit hooks to verify your commits::

    pip install pre-commit
    pre-commit install

The folder **test-project/** contains a pre-configured django project and
an SQlite database. Login for django admin is *admin:admin*::

    cd test-project
    python manage.py runserver

After this, navigate to `http://localhost:8000 <http://localhost:8000>`_


Community
---------

Please visit #django-wiki on irc.freenode.net as many django-wiki users
are also familiar with django-nyt which previously lived inside
django-wiki.

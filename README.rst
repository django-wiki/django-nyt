django-nyt
==========

django-nyt does this:

.. code:: python

    from django_nyt.utils import notify

    EVENT_KEY = "my_key"
    notify(_("OMG! Something happened"), EVENT_KEY)

All users subscribing to ``EVENT_KEY`` will have a notification created
in their stack. If you have emails enabled, they may get a summary of
notifications at an interval of their choice.

Data can be accessed easily from Django models or from the included JSON
views.

Why should you do this?
-----------------------

Users need a cleverly sifted stream of events that's highly customizable
as well. By using django-nyt, your users can subscribe to global events
or specific events pertaining specific objects.

Each event can be associated with a link so the user can use the
notifications as shortcuts in their work flow.

What do you need to do?
-----------------------

You need to do a lot! But django-nyt does everything to meet as many
needs as possible. Firstly, you need to write some javascript that will
fetch the latest notifications and display them in some area of the
screen. Upon clicking that icon, the latest notifications are displayed.
Something like this:

.. figure:: https://raw.githubusercontent.com/benjaoming/django-nyt/master/docs/misc/screenshot_dropdown.png
   :alt: Javascript drop-down

   Javascript drop-down
Some examples are provided, but there is no real easy way to place this
nifty little thing at the top of your site.

Other things for your TODO list:

-  Provide your users with options to customize their subscriptions and
   notification preferences
-  Customize contents of notification emails
-  Make the mail notification daemon script run
   ``python manage.py notifymail --daemon``
-  Put calls to ``notify(...)`` where ever necessary

Docs
----

Here:

http://django-nyt.readthedocs.org/en/latest/

Community
---------

Please visit #django-wiki on irc.freenode.net as many django-wiki users
are also familiar with django-nyt which previously lived inside
django-wiki.

Development
-----------

In your Git fork, run ``pip install -r requirements.txt`` to install the
requirements.

The folder **testproject/** contains a pre-configured django project and
an sqlite database. Login for django admin is *admin:admin*.

|Build Status|

|Downloads|

|Downloads|

|Wheel Status|

|Egg Status|

*This is a work in progre..*
----------------------------

Please refer to the
`TODO <https://github.com/benjaoming/django-nyt/blob/master/TODO.md>`__

.. |Build Status| image:: https://travis-ci.org/benjaoming/django-nyt.png?branch=master
   :target: https://travis-ci.org/benjaoming/django-nyt
.. |Downloads| image:: https://pypip.in/d/django-nyt/badge.png
   :target: https://pypi.python.org/pypi/django-nyt
.. |Downloads| image:: https://pypip.in/v/django-nyt/badge.png
   :target: https://pypi.python.org/pypi/django-nyt
.. |Wheel Status| image:: https://pypip.in/wheel/django-ny/badge.svg
   :target: https://pypi.python.org/pypi/django-nyt/
.. |Egg Status| image:: https://pypip.in/egg/django-nyt/badge.svg
   :target: https://pypi.python.org/pypi/django-nyt/

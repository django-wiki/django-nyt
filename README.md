django-nyt
=============

django_nyt does this:

```python
from django_nyt import notify

EVENT_KEY = "my_key"
notify(_("OMG! Something happened"), EVENT_KEY)
```

All users subscribing to `EVENT_KEY` will have a notification created in their
stack. If you have emails enabled, they may get a summary of notifications at an
interval of their choice.

Data can be accessed easily from Django models or from the included JSON views.

Why should you do this?
-----------------------

Users need an cleverly sifted stream of events. Ensure that they have the
possibility of customizing what they deem fit for their stream.

What do you need to do?
-----------------------

You need to do a lot. Firstly, you need to write some javascript that will
fetch the latest notifications and display them in some area of the screen.
Upon clicking that icon, the latest notifications are displayed. Something like
this:

![Javascript drop-down](https://raw2.github.com/benjaoming/django-nyt/master/docs/misc/screenshot_dropdown.png)

Some examples are provided, but there is no real easy way to place this nifty
little thing at the top of your site.

Other things for your TODO list:

 * Provide your users with options to customize their subscriptions and notification preferences.
 * Customize contents of notification emails
 * Make the mail notification daemon script run `python manage.py notifymail --daemon`
 * Put calls to `notify(...)` where ever necessary.

Docs
-----

Here:

http://django-nyt.readthedocs.org/en/latest/

Community
---------

Please visit #django-wiki on irc.freenode.net as many django-wiki users are also familiar with django-nyt which previously lived inside django-wiki.

*This is a work in progress*
----------------------------

Please refer to the [TODO](https://github.com/benjaoming/django-nyt/blob/master/TODO)

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

![Javascript drop-down](./docs/misc/screenshot_dropdown.png)

Here is a snippet example to get you started, but you need to get ui.js from [django-wiki/plugins/notifications](https://github.com/benjaoming/django-wiki/tree/master/wiki/plugins/notifications/static/wiki/plugins/notifications/js)
which is a couple of utility functions that use JQuery to get notifications from
a JSON view and display them in the right DOM element.

```html
<h2>Notifications:</h2>
<ul>
  <li class="notifications-empty"><a href="#"><em>{% trans "No notifications" %}</em></a></li>
  <li class="divider"></li>
  <li>
    <a href="#" onclick="notify_mark_read()">
      <i class="icon-check"></i>
      {% trans "Clear notifications list" %}
    </a>
  </li>
  <!-- Example of a settings page linked directly under the notifications -->
  <li>
    <a href="{% url 'wiki:notification_settings' %}">
      <i class="icon-wrench"></i>
      {% trans "Notification settings" %}
    </a>
  </li>
</ul>
<script type="text/javascript">
  URL_NOTIFY_GET_NEW = "{% url "notify:json_get" %}";
  URL_NOTIFY_MARK_READ = "{% url "notify:json_mark_read_base" %}";
  URL_NOTIFY_GOTO = "{% url "notify:goto_base" %}";
</script>
<script type="text/javascript" src="{{ STATIC_URL }}wiki/plugins/notifications/js/ui.js"></script>
```

Docs
-----

Here:

http://django-nyt.readthedocs.org/en/latest/

Community
---------

Please visit #django-wiki on irc.freenode.net as many django-wiki users are also familiar with django-nyt which previously lived inside django-wiki.


*This is a work in progress*
----------------------------

TODO:

 * Missing email functionality
 * Functions to easily retrive notifications and mark them as read
 * Some easy-to-use template tags and templates to override.
 * Examples of how to extend

How-to guides
=============

.. toctree::
   :maxdepth: 1
   :glob:

   *

Adding a notification
---------------------

.. code-block:: python

   from django_nyt.utils import notify

   EVENT_KEY = "my_key"
   notify(_("OMG! Something happened"), EVENT_KEY)


Subscribing to a specific object
--------------------------------

The Subscription model has a generic relation which can link it to any other object.
This means that aside from subscribing users to a universal event (i.e. "a comment was updated"),
users can also be subscribed to specific object (i.e. "*your* comment was updated").

.. code-block:: python

   notify(_("OMG! Something happened"), EVENT_KEY, target_object=my_model_instance)


Excluding certain recipients
----------------------------

By setting the kwarg ``filter_exclude`` to a dictionary of lookup fields for
``models.Subscription``, you may exclude certain users from getting a notification.

For instance, if a notification is solely for staff members, we can exclude all the users that aren't:

.. code-block:: python

   notify(
       _("OMG! Something happened"), EVENT_KEY,
       filter_exclude={'settings__user__is_staff': False}
   )


Disabling notifications
-----------------------

Use ``decorators.disable_notify`` to ensure that all notifications within a function are disabled.

For instance:

.. code-block:: python

   from django_nyt.decorators import disable_notify
   @disable_notify
   def my_view(request):
       ...


Case: Django-wiki integration
-----------------------------

Django-nyt is integrated with django-wiki by enabling ``wiki.plugins.notifications``.

Usage
=====

This is the overall picture: In your Python code, you call ``notify()`` with
some string message for the user, then in your browser application, you
should implement Websocket or polling based retrieval of those notifications
from a JSON view.

Python API
----------

Adding a notification
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from django_nyt.utils import notify
   
   EVENT_KEY = "my_key"
   notify(_("OMG! Something happened"), EVENT_KEY)


Adding a notification with a certain target object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Notification model has a GenericForeignKey which can link it to any other
object. This is nice, because you might have an intention to go the other way
around and ask "for this object, are there any notifications?"

.. code-block:: python

   notify(_("OMG! Something happened"), EVENT_KEY, target_object=my_model_instance)


Excluding certain recipients
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By setting the kwarg ``filter_exclude`` to a dictionary of lookup fields for
``models.Subscription``, you may exclude certain users from getting a notification.
For instance, if a notification is solely for staff members:

.. code-block:: html+django

   notify(
       _("OMG! Something happened"), EVENT_KEY, 
       filter_exclude={'settings__user__is_staff': True}
   )


Disabling notifications
~~~~~~~~~~~~~~~~~~~~~~~

Use ``decorators.disable_notify`` to ensure that all notifications within a function are disabled.

For instance:

.. code-block:: html+django

   from django_nyt.decorators import disable_notify
   @disable_notify
   def my_view(request):
       ...


JSON views
----------

The below views can be used for your JavaScript application. Examples of how to
use them is provided in :doc:`javascript`.

.. automodule:: django_nyt.views
   :members:
   :noindex:

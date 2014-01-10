Welcome to django-nyt's documentation!
======================================

Contents:

.. toctree::
   :maxdepth: 1

   installation
   configuration
   integration
   javascript

django-nyt
=============

Often a lot of stuff happens on a website, and users need an easy way to digest changes through notifications.

.. code-block:: python

   from django_nyt import notify
   
   EVENT_KEY = "my_key"
   notify(_("OMG! Something happened"), EVENT_KEY)


All users subscribing to ``EVENT_KEY`` will have a notification created in their
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

.. image:: misc/screenshot_dropdown.png

Try to refer to :doc:`javascript` -- it shows a pretty solid example of the UI logic that's needed for the above to work.

API Usage
---------

Adding a notification
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from django_nyt import notify
   
   EVENT_KEY = "my_key"
   notify(_("OMG! Something happened"), EVENT_KEY)


Adding a notification with a certain target object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Notification model has a GenericForeignKey which can link it to any other
object. This is nice, because you might have an intention to go the other way
around and ask "for this object, are there any notifications?"

.. code-block:: python

   notify(_("OMG! Something happened"), EVENT_KEY, target_object=my_model_instance)


Excluding certain recepients
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


*This is a work in progress*
----------------------------

This application should live outside django-wiki. 
It will! But only as soon as there's time to package it separately...

TODO:

 * A custom Model Manager to easily retrive notifications and mark them as read
 * Some easy-to-use template tags and templates to override.
 * Examples of how to extend


Indices and tables
==================

* :ref:``genindex``
* :ref:``modindex``
* :ref:``search``


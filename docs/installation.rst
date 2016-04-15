Installation
============

From PyPi
---------

Simply run the good old ``pip install django-nyt`` and you'll have the ``django_nyt`` package available.


Configuring your project
------------------------

Before django-nyt can be used, you need to migrate its models. This is also
necessary if you update it.

.. code-block:: bash

   python manage.py migrate django_nyt


INSTALLED_APPS
~~~~~~~~~~~~~~

.. code-block:: python

   INSTALLED_APPS = (
       ...
       'django_nyt'
       ...
   )


urlconf
~~~~~~~

You need to add the following patterns to get JSON views. You need to add it to your projects urlconf, typically ``urls.py``.

.. code-block:: python

   from django_nyt.urls import get_pattern as get_nyt_pattern
   urlpatterns += patterns('',
       url(r'^notifications/', get_nyt_pattern()),
   )

Or, for Django >= 1.8:

.. code-block:: python

   from django_nyt.urls import get_pattern as get_nyt_pattern
   urlpatterns += [
       url(r'^notifications/', get_nyt_pattern()),
   ]

Installation
============

From PyPi
---------

Simply run the good old ``pip install django-nyt`` and you'll have the ``django_nyt`` package available.

Adding to your Python project
-----------------------------

.. code-block:: bash

   python manage.py migrate django_nyt


Configuring your django project
-------------------------------

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


Django < 1.7
~~~~~~~~~~~~

If you run older versions of django, please ensure that South is using the
`south_migrations` module, and not the default `migrations` module which is
now for Django 1.7. 

::

    INSTALLED_APPS += ['south',]
    SOUTH_MIGRATION_MODULES = {
        'django_nyt': 'django_nyt.south_migrations',
    }

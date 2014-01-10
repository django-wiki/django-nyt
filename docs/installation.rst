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
       (r'^nyt/', get_nyt_pattern()),
   )


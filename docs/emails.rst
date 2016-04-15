Email digests
-------------

A management script is supplied for sending out emails.

Here are 3 alternative ways of getting email notifications sent out:

 #. As a Celery task
 #. As a daemon
 #. As a cronjob


Celery integration
~~~~~~~~~~~~~~~~~~

If you use Celery, you could probably see it easily done to add a simple
scheduled task with Celery Beat that calls

If you don't use Celery already, we cannot recommend to deploy Celery simply for
the sake of sending out these emails. Instead, it's probably easier to use one
of the other methods.

You need to run something like this:

.. code-block:: python
    
    from django.core.management import call_command
    
    @shared_task
    def send_nyt_emails()
        call_command('notifymail', cron=True)


Schedule the task as often as you want instant email notifications to be
guaranteed to reach the user. If you are using channels, you don't need to
worry about instant notifications as they're sent asynchronously in this case.

You can also hook the scheduling of the task to the ``post_save`` signal on
``django_nyt.models.Notification`` (TODO: write example code).


Crontab
~~~~~~~

Schedule the task as often as you want instant email notifications to be
guaranteed to reach the user. If you are using channels, you don't need to
worry about instant notifications as they're sent asynchronously in this case.

.. code-block:: bash
    
    sudo su YOUR_HTTPD_USER -c bash  # e.g. www-data
    crontab -e  # Edit the cron tab

This is the code you should add to your crontab:

.. code-block:: bash

    /path/to/your/virtualenv/bin/python /path/to/project/manage.py notifymail --cron


Daemon
~~~~~~

Instead of adding a crontab, you can also have the ``notifymail`` script run as
a daemon.

.. code-block:: bash

    /path/to/your/virtualenv/bin/python /path/to/project/manage.py notifymail --daemon

For more configurability of the daemon, run ``manage.py help notifymail``.

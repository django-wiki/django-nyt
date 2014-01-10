JavaScript and HTML
===================

In order to really make use of a notification system, you would probably want a small icon in the top corner of your websites. Like the privacy destroying
villains at facebook have. Or the wonderful innovation heroes at Github have.

Method:

 1. Put all your logic in your own ui.js file. There is so much presentation logic in this stuff, that we can hardly ship anything useful.
    You have to build that from scratch.
 2. Initialize your javascript environment with the URLs necessary to use your js file:

.. code-block:: html+django

   <script type="text/javascript">
     URL_NOTIFY_GET_NEW = "{% url "notify:json_get" %}";
     URL_NOTIFY_MARK_READ = "{% url "notify:json_mark_read_base" %}";
     URL_NOTIFY_GOTO = "{% url "notify:goto_base" %}";
   </script>
   <script type="text/javascript" src="{{ STATIC_URL }}notifications/js/ui.js"></script>


Example ui.js
-------------

**YOU NEED JQUERY**

Create the necessary elements for this javascript to run, and you should have a pretty useful little menu at the top of your website.

.. code-block:: javascript

    notify_oldest_id = 0;
    notify_latest_id = 0;
    notify_update_timeout = 30000;
    notify_update_timeout_adjust = 1.2; // factor to adjust between each timeout.

    function notify_update() {
      jsonWrapper(URL_NOTIFY_GET_NEW+notify_latest_id+'/', function (data) {
        if (data.success) {
          $('.notification-cnt').html(data.total_count);
          if (data.objects.length> 0) {
            $('.notification-cnt').addClass('badge-important');
            $('.notifications-empty').hide();
          } else {
            $('.notification-cnt').removeClass('badge-important');
          }
          for (var i=data.objects.length-1; i >=0 ; i--) {
            n = data.objects[i];
            notify_latest_id = n.pk>notify_latest_id ? n.pk:notify_latest_id;
            notify_oldest_id = (n.pk<notify_oldest_id || notify_oldest_id==0) ? n.pk:notify_oldest_id;
            if (n.occurrences > 1) {
              element = $('<li><a href="'+URL_NOTIFY_GOTO+n.pk+'/"><div>'+n.message+'</div><div class="since">'+n.occurrences_msg+' - ' + n.since + '</div></a></li>')
            } else {
              element = $('<li><a href="'+URL_NOTIFY_GOTO+n.pk+'/"><div>'+n.message+'</div><div class="since">'+n.since+'</div></a></li>');
            }
            element.addClass('notification-li');
            element.insertAfter('.notification-before-list');
          }
        }
      });
    }

    function notify_mark_read() {
      $('.notification-li-container').empty();
      url = URL_NOTIFY_MARK_READ+notify_latest_id+'/'+notify_oldest_id+'/';
      notify_oldest_id = 0;
      notify_latest_id = 0;
      jsonWrapper(url, function (data) {
        if (data.success) {
          notify_update();
        }
      });
    }

    function update_timeout() {
      setTimeout("notify_update()", notify_update_timeout);
      setTimeout("update_timeout()", notify_update_timeout);
      notify_update_timeout *= notify_update_timeout_adjust;
    }

    $(document).ready(function () {
      update_timeout();
    });

    // Don't check immediately... some users just click through pages very quickly.
    setTimeout("notify_update()", 2000);


Example HTML
------------

.. code-block:: html+django

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

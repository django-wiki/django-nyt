Channels & websockets
=====================

Avoiding constant polling is important because:

 #. polling is repetitive and unnecessary
 #. each request occupies the whole django application stack
 #. whatever your polling interval, it's not real time!

Now, django-nyt comes with pre-configured tasks for django-channels and
JavaScript snippets that will help you to quickly get started. Just follow the
steps below.

Configure channels
------------------
 
You need channels to be running a websocket server. The below example can be
used for a development server, but other than that, you would have to configure
a real integration with a channel worker server and Redis.

.. code-block:: python

    INSTALLED_APPS.append('channels')
    CHANNEL_LAYERS = {
        "default": {
            "BACKEND": "asgiref.inmemory.ChannelLayer",
            "ROUTING": "django_nyt.routing.channel_routing",
        },
    }


For more on deployment, read `the Channels documentation <http://channels.readthedocs.org/en/latest/deploying.html>`_.


Communicating with websockets
-----------------------------

On the client-side, meaning in your Django templates and static files, you
need to add some JavaScript to make everything work. This is the essential
stuff, copy it where ever you deem fit (it needs JQuery loaded):

The essential bit below is to customize the various HTML DOM elements that are
mentioned, but you can also use the same CSS class names as defined in
:doc:`html`.

.. code-block:: html+django

    <script type="text/javascript">
      var URL_NYT_GET_NEW = "{% url "nyt:json_get" %}";
      var URL_NYT_MARK_READ = "{% url "nyt:json_mark_read_base" %}";
      var URL_NYT_GOTO = "{% url "nyt:goto_base" %}";
    
      var nyt_oldest_id = 0;
      var nyt_latest_id = 0;
      var nyt_update_timeout = 30000;
      var nyt_update_timeout_adjust = 1.2; // factor to adjust between each timeout.
      
      // Customixed error handling?
      function ajaxError(){}
      
      $.ajaxSetup({
        timeout: 7000,
        cache: false,
        error: function(e, xhr, settings, exception) {
            ajaxError();
        }
      });
      
      function jsonWrapper(url, callback) {
        $.getJSON(url, function(data) {
          if (data == null) {
            ajaxError();
          } else {
            callback(data);
          }
        });
      }
    
      function nyt_update() {
        jsonWrapper(URL_NYT_GET_NEW+nyt_latest_id+'/', function (data) {
          if (data.success) {
            $('.notification-cnt').html(data.total_count);
            if (data.objects.length> 0) {
              $('.notification-cnt').addClass('badge-important');
              $('.notifications-empty').hide();
            } else {
              $('.notification-cnt').removeClass('badge-important');
            }
            for (var i=data.objects.length-1; i >=0 ; i--) {
              var n = data.objects[i];
              nyt_latest_id = n.pk>nyt_latest_id ? n.pk:nyt_latest_id;
              nyt_oldest_id = (n.pk<nyt_oldest_id || nyt_oldest_id==0) ? n.pk:nyt_oldest_id;
              if (n.occurrences > 1) {
                element = $('<li><a href="'+URL_NYT_GOTO+n.pk+'/"><span>'+n.message+'</span> <span class="since">'+n.occurrences_msg+' - ' + n.since + '</span></a></li>')
              } else {
                element = $('<li><a href="'+URL_NYT_GOTO+n.pk+'/"><span>'+n.message+'</span> <span class="since">'+n.since+'</span></a></li>');
              }
              element.addClass('notification-li');
              element.hide();
              element.insertAfter('.notification-before-list');
              element.show('slow');
            }
          }
        });
      }
    
      // Mark all <li> items read and tell the server.
      function nyt_mark_read() {
        $('.notification-li').remove();
        var url = URL_NYT_MARK_READ+nyt_latest_id+'/'+nyt_oldest_id+'/';
        nyt_oldest_id = 0;
        nyt_latest_id = 0;
        jsonWrapper(url, function (data) {
          if (data.success) {
            $('.notifications-empty').show();
            nyt_update();
          }
        });
      }
    
      // Call this function to use traditional polling
      function update_timeout() {
        setTimeout("nyt_update()", nyt_update_timeout);
        setTimeout("update_timeout()", nyt_update_timeout);
        nyt_update_timeout *= nyt_update_timeout_adjust;
      }
    
      // Don't check immediately... some users just click through pages very quickly.
      setTimeout("nyt_update()", 2000);
    
      var socket = new WebSocket("ws://127.0.0.1:8000/nyt");
    
      $(document).ready(function () {
        // update_timeout();
        socket.onopen = function() {
            console.log("Sending hello world");
            socket.send("hello world");
        }
        socket.onmessage = function(e) {
          console.log("Got some message, so going to update");
          nyt_update();
        }
    
      });
    
    </script>



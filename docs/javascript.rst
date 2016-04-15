JavaScript polling
==================



In order to really make use of a notification system, you would probably want a small icon in the top corner of your websites. Like the privacy destroying
villains at facebook have. Or the wonderful innovation heroes at Github have.

Method:

 1. Put all your logic in your own ui.js file. There is so much presentation logic in this stuff, that we can hardly ship anything useful.
    You have to build that from scratch.
 2. Initialize your javascript environment with the URLs necessary to use your js file:

.. code-block:: html+django

   <script type="text/javascript">
     URL_NYT_GET_NEW = "{% url "nyt:json_get" %}";
     URL_NYT_MARK_READ = "{% url "nyt:json_mark_read_base" %}";
     URL_NYT_GOTO = "{% url "nyt:goto_base" %}";
   </script>
   <!-- A custom script that you need to implement yourself using example code below -->
   <script type="text/javascript" src="{{ STATIC_URL }}notifications/js/ui.js"></script>


Example ui.js
-------------

**YOU NEED JQUERY**

Create the necessary elements for this javascript to run, and you should have a pretty useful little menu at the top of your website.

.. code-block:: javascript

    var nyt_oldest_id = 0;
    var nyt_latest_id = 0;
    var nyt_update_timeout = 30000;
    var nyt_update_timeout_adjust = 1.2; // factor to adjust between each timeout.
    
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
              element = $('<li><a href="'+URL_NYT_GOTO+n.pk+'/"><div>'+n.message+'</div><div class="since">'+n.occurrences_msg+' - ' + n.since + '</div></a></li>')
            } else {
              element = $('<li><a href="'+URL_NYT_GOTO+n.pk+'/"><div>'+n.message+'</div><div class="since">'+n.since+'</div></a></li>');
            }
            element.addClass('notification-li');
            element.insertAfter('.notification-before-list');
          }
        }
      });
    }

    function nyt_mark_read() {
      $('.notification-li-container').empty();
      url = URL_NYT_MARK_READ+nyt_latest_id+'/'+nyt_oldest_id+'/';
      nyt_oldest_id = 0;
      nyt_latest_id = 0;
      jsonWrapper(url, function (data) {
        if (data.success) {
          nyt_update();
        }
      });
    }

    function update_timeout() {
      setTimeout("nyt_update()", nyt_update_timeout);
      setTimeout("update_timeout()", nyt_update_timeout);
      nyt_update_timeout *= nyt_update_timeout_adjust;
    }

    $(document).ready(function () {
      update_timeout();
    });

    // Don't check immediately... some users just click through pages very quickly.
    setTimeout("nyt_update()", 2000);

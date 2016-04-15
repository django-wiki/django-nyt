Example HTML
============

In order for the example JavaScript for websockets and snippets to work, we
have assumed a list with notifications. The list contains a
``.notification-before-list`` element which indicates to the JavaScript code
that all ``<li>``'s should be appended after this element. Inside this element,
we also have the ``.notification-cnt`` which is updated every time new
notifications arrive or are marked as read.

.. code-block:: html+django

    <h2>Notifications:</h2>
    <ul>
      <li class="notification-before-list">Notifications (<span class="badge notification-cnt">0</span>):</li>
      <li class="notifications-empty"><a href="#"><em>{% trans "No notifications" %}</em></a></li>
    </ul>

    <a href="#" onclick="nyt_mark_read()">
      <i class="icon-check"></i>
      {% trans "Clear notifications list" %}
    </a>

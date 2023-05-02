from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.utils.translation import gettext as _

from django_nyt import models
from django_nyt.decorators import json_view
from django_nyt.decorators import login_required_ajax


@login_required_ajax
@json_view
def get_notifications(request, latest_id=None, is_viewed=False, max_results=10):
    """
    View that returns a JSON list of notifications for the current user as according
    to ``request.user``.

    :param: latest_id: The latest id of a notification. Use this to avoid
    retrieving the same notifications multiple times.
    :param: is_viewed: Set this to ``True`` if you also want to retrieve
    notifications that have already been viewed.

    :returns: An HTTPResponse object with JSON data::

        {'success': True,
         'total_count': total_count,
         'objects': [{'pk': n.pk,
                     'message': n.message,
                     'url': n.url,
                     'occurrences': n.occurrences,
                     'occurrences_msg': _('%d times') % n.occurrences,
                     'type': n.subscription.notification_type.key if n.subscription else None,
                     'since': naturaltime(n.created)} for n in notifications[:max_results]]}
    """

    notifications = models.Notification.objects.filter(
        Q(subscription__settings__user=request.user) | Q(user=request.user),
    )

    if is_viewed is not None:
        notifications = notifications.filter(is_viewed=is_viewed)

    total_count = notifications.count()

    if latest_id is not None:
        notifications = notifications.filter(id__gt=latest_id)

    notifications = notifications.order_by("-id")
    notifications = notifications.prefetch_related(
        "subscription", "subscription__notification_type"
    )

    from django.contrib.humanize.templatetags.humanize import naturaltime

    return {
        "success": True,
        "total_count": total_count,
        "objects": [
            {
                "pk": n.pk,
                "message": n.message,
                "url": n.url,
                "occurrences": n.occurrences,
                "occurrences_msg": _("%d times") % n.occurrences,
                "type": n.subscription.notification_type.key
                if n.subscription
                else None,
                "since": naturaltime(n.created),
            }
            for n in notifications[:max_results]
        ],
    }


@login_required
def goto(request, notification_id=None):
    referer = request.META.get("HTTP_REFERER", "")
    if not notification_id:
        return redirect(referer)
    notification = get_object_or_404(
        models.Notification,
        Q(subscription__settings__user=request.user) | Q(user=request.user),
        id=notification_id,
    )
    notification.is_viewed = True
    notification.save()
    if notification.url:
        return redirect(notification.url)
    return redirect(referer)


@login_required_ajax
@json_view
def mark_read(request, id_lte, notification_type_id=None, id_gte=None):

    notifications = models.Notification.objects.filter(
        Q(subscription__settings__user=request.user) | Q(user=request.user),
        id__lte=id_lte,
    )

    if notification_type_id:
        notifications = notifications.filter(notification_type__id=notification_type_id)

    if id_gte:
        notifications = notifications.filter(id__gte=id_gte)

    notifications.update(is_viewed=True)

    return {"success": True}

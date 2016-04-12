from __future__ import unicode_literals

import logging

from django_nyt.utils import notify

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext as _

logger = logging.getLogger(__name__)

NOTIFICATION_TEST_KEY = "testapp_stuff_was_created"


class TestModel(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return "Test object: {}".format(self.name)

    class Meta:
        verbose_name = "Test"


@receiver(post_save, sender=TestModel)
def notify_test(sender, instance, **kwargs):

    logger.info("New object created: {}".format(str(instance)))

    notify(
        _("Message is: {}".format(instance.name)),
        NOTIFICATION_TEST_KEY,
        target_object=instance,
    )

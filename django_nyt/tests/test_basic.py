from __future__ import absolute_import
from __future__ import unicode_literals
from django.test import TestCase

from django_nyt import utils, models

try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
except ImportError:
    from django.contrib.auth.models import User


class NotifyTest(TestCase):

    def test_simple(self):

        TEST_KEY = 'test_key'
        user = User.objects.create_user(
            'lalala'
        )
        user_settings = models.Settings.objects.create(user=user)
        utils.subscribe(user_settings, TEST_KEY)
        utils.notify("Test Is a Test", TEST_KEY)

        self.assertEqual(models.Notification.objects.all().count(), 1)

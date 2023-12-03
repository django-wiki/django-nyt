from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from django_nyt import models
from django_nyt import utils


User = get_user_model()


class TestViews(TestCase):
    def setUp(self):
        super().setUp()
        self.TEST_KEY = "test_key"
        self.user = User.objects.create_user(
            "lalala",
            password="password",
        )
        self.user_settings = models.Settings.get_default_setting(self.user)

    def tearDown(self):
        super().tearDown()
        models._notification_type_cache = {}

    def test_mark_read(self):
        utils.subscribe(self.user_settings, self.TEST_KEY)
        utils.notify("Test Is a Test", self.TEST_KEY)
        self.assertEqual(models.Notification.objects.filter(is_viewed=False).count(), 1)
        nid = models.Notification.objects.get().id
        self.client.login(username=self.user.username, password="password")
        self.client.get(reverse("nyt:json_mark_read", args=(nid,)))
        self.assertEqual(models.Notification.objects.filter(is_viewed=False).count(), 0)

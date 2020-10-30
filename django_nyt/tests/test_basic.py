from django.contrib.auth import get_user_model
from django.test import TestCase

from django_nyt import models
from django_nyt import utils

User = get_user_model()


class NotifyTestBase(TestCase):

    def setUp(self):
        super(NotifyTestBase, self).setUp()
        self.TEST_KEY = 'test_key'

        # These two users are created by migrations in testproject.testapp
        # Reason is to make the testproject easy to setup and use.
        self.user1 = User.objects.get(username='alice')
        self.user1_settings = models.Settings.get_default_setting(self.user1)
        self.user2 = User.objects.get(username='bob')
        self.user2_settings = models.Settings.get_default_setting(self.user2)

    def tearDown(self):
        self.user1.delete()
        self.user2.delete()
        models._notification_type_cache = {}
        super().tearDown()


class NotifyTest(NotifyTestBase):

    def test_notify(self):

        # Subscribe User 1 to test key
        utils.subscribe(self.user1_settings, self.TEST_KEY)
        utils.notify("Test is a test", self.TEST_KEY)

        # Check that there is exactly 1 notification
        self.assertEqual(models.Notification.objects.all().count(), 1)

    def test_notify_two_users(self):

        # Subscribe User 2 to test key
        utils.subscribe(self.user2_settings, self.TEST_KEY)
        utils.subscribe(self.user1_settings, self.TEST_KEY)
        utils.notify("Another test", self.TEST_KEY)

        self.assertEqual(models.Notification.objects.all().count(), 2)

        # Now create the same notification again, this should not create new
        # objects in the DB but instead increase the count of that notification!
        utils.notify("Another test", self.TEST_KEY)

        self.assertEqual(models.Notification.objects.filter(occurrences=2).count(), 2)

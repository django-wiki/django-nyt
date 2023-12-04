from .test_basic import NotifyTestBase
from django_nyt import models
from django_nyt import utils


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

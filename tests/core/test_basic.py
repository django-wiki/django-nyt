from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase

from django_nyt import models
from django_nyt import utils
from django_nyt.conf import WEEKLY
from django_nyt.decorators import disable_notify
from django_nyt.models import Settings
from tests.testapp.models import TestModel

User = get_user_model()


class NotifyTestBase(TestCase):

    TEST_KEY = "test_key"

    def setUp(self):
        super(NotifyTestBase, self).setUp()
        models._notification_type_cache = {}

        # These two users are created by migrations in testproject.testapp
        # Reason is to make the testproject easy to setup and use.
        self.user1 = User.objects.get(username="alice")
        self.user1_settings = models.Settings.get_default_setting(self.user1)
        self.user2 = User.objects.get(username="bob")
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

    def test_disable_notify(self):
        # Subscribe User 1 to test key
        utils.subscribe(self.user1_settings, self.TEST_KEY)

        @disable_notify
        def inner():
            utils.notify("Test is a test", self.TEST_KEY)

        inner()

        # Check that there is exactly 1 notification
        self.assertEqual(models.Notification.objects.all().count(), 0)

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

    def test_failure_target_object_not_model(self):

        # Subscribe User 1 to test key
        utils.subscribe(self.user1_settings, self.TEST_KEY)
        with self.assertRaises(TypeError):
            utils.notify("Another test", self.TEST_KEY, target_object=object())

    def test_with_target_object(self):

        related_object = TestModel.objects.create(name="test_with_target_object")
        content_type = ContentType.objects.get_for_model(TestModel)
        # Subscribe User 1 to test key
        utils.subscribe(
            self.user1_settings,
            self.TEST_KEY,
            content_type=content_type,
            object_id=related_object.id,
        )
        utils.notify("Test related object", self.TEST_KEY, target_object=related_object)

        self.assertEqual(
            models.Notification.objects.filter(
                subscription__object_id=related_object.id,
                subscription__notification_type__content_type=content_type,
            ).count(),
            1,
        )

    def test_unsubscribe(self):

        related_object = TestModel.objects.create(name="test_with_target_object")
        content_type = ContentType.objects.get_for_model(TestModel)
        # Subscribe User 1 to test key
        utils.subscribe(
            self.user1_settings,
            self.TEST_KEY,
            content_type=content_type,
            object_id=related_object.id,
        )
        # Subscribe User 1 to test key without content type
        utils.subscribe(
            self.user1_settings,
            self.TEST_KEY,
        )
        utils.notify("Test related object", self.TEST_KEY, target_object=related_object)

        # Test also that notifications aren't deleted
        notifications_before = models.Notification.objects.all().count()

        utils.unsubscribe(
            self.TEST_KEY,
            settings=self.user1_settings,
            content_type=content_type,
            object_id=related_object.id,
        )

        assert notifications_before == models.Notification.objects.all().count()

        # Check that exactly 1 notification is generated (no content type filter)
        utils.notify("Test related object", self.TEST_KEY, target_object=related_object)
        assert models.Notification.objects.all().count() == notifications_before + 1

        # And now we unsubscribe the remaining!
        utils.unsubscribe(
            self.TEST_KEY,
            user=self.user1_settings.user,
        )

        assert models.Notification.objects.all().count() == notifications_before + 1

        # Check that no notification is generated here
        utils.notify("Test related object", self.TEST_KEY)
        assert models.Notification.objects.all().count() == notifications_before + 1


class NotifySettingsTest(NotifyTestBase):
    def test_create_settings(self):
        # Create another user setting

        Settings.objects.create(user=self.user1, interval=WEEKLY, is_default=False)
        assert Settings.objects.filter(user=self.user1, is_default=True).count() == 1
        assert Settings.objects.filter(user=self.user1).count() == 2

        Settings.objects.create(user=self.user1, interval=WEEKLY, is_default=True)
        assert Settings.objects.filter(user=self.user1, is_default=True).count() == 1
        assert Settings.objects.filter(user=self.user1).count() == 3

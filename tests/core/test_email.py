from django.core import mail
from django.core.management import call_command

from .test_basic import NotifyTestBase
from django_nyt import models
from django_nyt import utils


class NotifyTest(NotifyTestBase):
    def test_notify(self):
        mail.outbox = []

        # Subscribe User 1 to test key
        utils.subscribe(self.user1_settings, self.TEST_KEY, send_emails=True)
        utils.notify("Test is a test", self.TEST_KEY)

        call_command("notifymail", "--cron", "--no-sys-exit")

        assert len(mail.outbox) == 1
        assert mail.outbox[0].subject == "You have new notifications"
        assert (
            mail.outbox[0].body
            == """Dear alice,

These are the instantly notifications from example.com.

 * Test is a test
   http://example.comNone


Thanks for using our site!

Sincerely,
example.com

"""
        )

        # Check that there is exactly 1 notification
        self.assertEqual(models.Notification.objects.all().count(), 1)

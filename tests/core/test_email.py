from collections import OrderedDict

from django.core import mail
from django.core.management import call_command
from django.test import override_settings

from .test_basic import NotifyTestBase
from django_nyt import utils


class NotifyTest(NotifyTestBase):
    def test_notify(self):
        mail.outbox = []

        # Subscribe User 1 to test key
        utils.subscribe(self.user1_settings, self.TEST_KEY, send_emails=True)
        utils.notify("Test is a test", self.TEST_KEY)

        call_command("notifymail", "--cron", "--no-sys-exit")

        assert len(mail.outbox) == 1
        assert (
            mail.outbox[0].subject
            == "You have new notifications from example.com (type: instantly)"
        )
        assert (
            mail.outbox[0].body
            == """Dear alice,

These are notifications sent instantly from example.com.

 * Test is a test


Thanks for using our site!

Sincerely,
example.com

"""
        )

    def test_notify_with_url(self):
        mail.outbox = []

        # Subscribe User 1 to test key
        utils.subscribe(self.user1_settings, self.TEST_KEY, send_emails=True)
        utils.notify("Test is a test", self.TEST_KEY, url="/test")

        call_command("notifymail", "--cron", "--no-sys-exit")

        assert len(mail.outbox) == 1
        assert (
            mail.outbox[0].subject
            == "You have new notifications from example.com (type: instantly)"
        )
        assert (
            mail.outbox[0].body
            == """Dear alice,

These are notifications sent instantly from example.com.

 * Test is a test
   https://example.com/test


Thanks for using our site!

Sincerely,
example.com

"""
        )

    @override_settings(
        NYT_EMAIL_TEMPLATE_NAMES=OrderedDict(
            {NotifyTestBase.TEST_KEY: "testapp/notifications/email.txt"}
        ),
        NYT_EMAIL_SUBJECT_TEMPLATE_NAMES=OrderedDict(
            {NotifyTestBase.TEST_KEY: "testapp/notifications/email_subject.txt"}
        ),
    )
    def test_custom_email_template(self):

        mail.outbox = []

        # Subscribe User 1 to test key
        utils.subscribe(self.user1_settings, self.TEST_KEY, send_emails=True)
        utils.notify("Test is a test", self.TEST_KEY, url="/test")

        call_command("notifymail", "--cron", "--no-sys-exit")

        assert len(mail.outbox) == 1
        assert mail.outbox[0].subject == "subject"
        assert mail.outbox[0].body == "Test\n"

    @override_settings(
        NYT_EMAIL_TEMPLATE_NAMES=OrderedDict(
            [
                ("key1", "testapp/notifications/email.txt"),
                ("admin_*", "testapp/notifications/admin.txt"),
            ]
        ),
        NYT_EMAIL_SUBJECT_TEMPLATE_NAMES=OrderedDict(
            [
                ("key1", "testapp/notifications/email_subject.txt"),
                ("admin_*", "testapp/notifications/admin_subject.txt"),
                ("*", "notifications/emails/default_subject.txt"),
            ]
        ),
    )
    def test_multiple_templates(self):

        # Subscribe User 1 to 3 keys
        utils.subscribe(self.user1_settings, "key1", send_emails=True)
        utils.subscribe(self.user1_settings, "admin_emails", send_emails=True)
        utils.subscribe(self.user1_settings, "key2", send_emails=True)
        utils.subscribe(self.user1_settings, "key3", send_emails=False)

        mail.outbox = []
        utils.notify("Specific key1 test", "key1", url="/test-key1")
        utils.notify("Default test", "key2", url="/test")
        utils.notify("Admin test", "admin_emails", url="/test")

        call_command("notifymail", "--cron", "--no-sys-exit")

        assert len(mail.outbox) == 3
        assert mail.outbox[0].subject == "subject"
        assert mail.outbox[0].body == "Test\n"
        assert mail.outbox[1].body == "Admin\n"
        assert mail.outbox[1].subject == "notifications for admin"
        assert (
            mail.outbox[2].subject
            == "You have new notifications from example.com (type: instantly)"
        )

    @override_settings(NYT_EMAIL_SUBJECT="test")
    def test_nyt_email_subject(self):

        mail.outbox = []

        # Subscribe User 1 to test key
        utils.subscribe(self.user1_settings, self.TEST_KEY, send_emails=True)
        utils.notify("Test is a test", self.TEST_KEY, url="/test")

        call_command("notifymail", "--cron", "--no-sys-exit")

        assert len(mail.outbox) == 1
        assert mail.outbox[0].subject == "test"

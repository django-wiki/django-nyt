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
        # TODO: https://github.com/django-wiki/django-nyt/issues/124
        from django_nyt import settings as nyt_settings

        nyt_settings.EMAIL_TEMPLATE_NAMES = OrderedDict(
            {NotifyTestBase.TEST_KEY: "testapp/notifications/email.txt"}
        )
        nyt_settings.EMAIL_SUBJECT_TEMPLATE_NAMES = OrderedDict(
            {NotifyTestBase.TEST_KEY: "testapp/notifications/email_subject.txt"}
        )

        mail.outbox = []

        # Subscribe User 1 to test key
        utils.subscribe(self.user1_settings, self.TEST_KEY, send_emails=True)
        utils.notify("Test is a test", self.TEST_KEY, url="/test")

        call_command("notifymail", "--cron", "--no-sys-exit")

        assert len(mail.outbox) == 1
        assert mail.outbox[0].subject == "subject"
        assert mail.outbox[0].body == "Test\n"

        # Reset to default state
        # TODO: https://github.com/django-wiki/django-nyt/issues/124
        nyt_settings.EMAIL_TEMPLATE_NAMES = OrderedDict()
        nyt_settings.EMAIL_SUBJECT_TEMPLATE_NAMES = OrderedDict()

    @override_settings(NYT_EMAIL_SUBJECT="test")
    def test_nyt_email_subject(self):

        # TODO: https://github.com/django-wiki/django-nyt/issues/124
        from django_nyt import settings as nyt_settings

        old_setting = nyt_settings.EMAIL_SUBJECT
        nyt_settings.EMAIL_SUBJECT = "test"

        mail.outbox = []

        # Subscribe User 1 to test key
        utils.subscribe(self.user1_settings, self.TEST_KEY, send_emails=True)
        utils.notify("Test is a test", self.TEST_KEY, url="/test")

        call_command("notifymail", "--cron", "--no-sys-exit")

        assert len(mail.outbox) == 1
        assert mail.outbox[0].subject == "test"

        # Reset to default state
        # TODO: https://github.com/django-wiki/django-nyt/issues/124
        nyt_settings.EMAIL_SUBJECT = old_setting

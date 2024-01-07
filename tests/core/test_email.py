import re
from collections import OrderedDict
from datetime import timedelta

import pytest
from django.core import mail
from django.core.management import call_command
from django.test import override_settings
from django.utils import timezone

from .test_basic import NotifyTestBase
from django_nyt import models
from django_nyt import utils
from django_nyt.conf import WEEKLY


@pytest.mark.django_db
def test_glob_matching():
    test_cases = [
        # path, pattern, new_should_match
        ("/path/to/foo", "*", False),
        ("/path/to/foo", "**", True),
        ("/path/to/foo", "/path/*", False),
        ("/path/to/foo", "/path/**", True),
        ("/path/to/foo", "/path/to/*", True),
        ("/path/to", "/path?to", False),
        ("/path/to", "/path[!abc]to", False),
        ("/pathlalato", "/path[a-z]*to", True),
        ("/path-to", "/path-*", True),
        ("/path-[to", "/path-[*", True),
        ("admin/user/notification", "admin/**", True),
        ("WHATEVER", "*", True),
        ("WHATEVER/BUT/NOT/THIS", "*", False),
        ("admin/user/notification", "admin/**/*", True),
    ]

    for path, pattern, new_should_match in test_cases:
        new_re = re.compile(models._glob_to_re(pattern))
        new_match = bool(new_re.match(path))
        if new_match is not new_should_match:
            raise AssertionError(
                f"regex from `glob_to_re()` should match path "
                f"'{path}' when given pattern: {pattern}"
            )


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

    def test_notify_with_url_domain(self):
        mail.outbox = []

        # Subscribe User 1 to test key
        utils.subscribe(self.user1_settings, self.TEST_KEY, send_emails=True)
        utils.notify("Test is a test", self.TEST_KEY, url="/test")

        call_command("notifymail", "--cron", "--no-sys-exit", "--domain=foobar.com")

        assert len(mail.outbox) == 1
        assert (
            mail.outbox[0].subject
            == "You have new notifications from foobar.com (type: instantly)"
        )
        assert (
            mail.outbox[0].body
            == """Dear alice,

These are notifications sent instantly from foobar.com.

 * Test is a test
   https://foobar.com/test


Thanks for using our site!

Sincerely,
foobar.com

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

        assert mail.outbox[1].subject == "subject"
        assert mail.outbox[1].body == "Test\n"
        assert mail.outbox[0].body == "Admin\n"
        assert mail.outbox[0].subject == "notifications for admin"
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


class NotifyTestWeekly(NotifyTestBase):
    def test_notify_weekly_nothing_sent_first_week(self):

        user1_weekly_setting = models.Settings.objects.create(
            user=self.user1_settings.user,
            interval=WEEKLY,
        )

        mail.outbox = []

        # Subscribe User 1 to test key for weekly notifications
        utils.subscribe(user1_weekly_setting, self.TEST_KEY, send_emails=True)

        # Create a notification
        utils.notify("Test is a test", self.TEST_KEY)

        call_command("notifymail", "--cron", "--no-sys-exit")

        # Ensure nothing is sent, a week hasn't passed
        assert len(mail.outbox) == 0

        # Ensure something is sent if we try a week from now
        mail.outbox = []
        call_command(
            "notifymail",
            "--cron",
            "--no-sys-exit",
            now=timezone.now() + timedelta(minutes=WEEKLY + 1),
        )
        assert len(mail.outbox) == 1
        assert "weekly" in mail.outbox[0].subject

        # Now ensure that we receive an instant notification regardless of the previous weekly notification
        utils.subscribe(self.user1_settings, self.TEST_KEY, send_emails=True)
        notifications = utils.notify("This is a second test", self.TEST_KEY)
        print("hello")
        print(notifications[0].subscription.notification_type)
        print(notifications[0].subscription.settings.id)
        print(self.user1_settings.id)
        assert (
            models.Notification.objects.filter(
                subscription__notification_type__key=self.TEST_KEY,
                subscription__settings=self.user1_settings,
            ).count()
            == 1
        )
        mail.outbox = []
        call_command("notifymail", "--cron", "--no-sys-exit")
        assert len(mail.outbox) == 1

        # Now fast-forward and ensure that the notification is found in the weekly digest
        ...

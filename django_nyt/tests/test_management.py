import os
import signal
import time
from tempfile import NamedTemporaryFile

from django.core.management import call_command

from .. import models, utils
from .test_basic import NotifyTestBase


class CommandTest(NotifyTestBase):

    def test_notifymail(self):

        utils.subscribe(self.user2_settings, self.TEST_KEY)
        utils.subscribe(self.user1_settings, self.TEST_KEY)
        utils.notify("This notification goes out by mail!", self.TEST_KEY)

        call_command("notifymail", cron=True)

        # No un-mailed notifications can be left!
        self.assertEqual(models.Notification.objects.filter(is_emailed=False).count(), 0)

        # Test that calling it again works but nothing gets sent
        call_command("notifymail", cron=True)

        # Now try the daemon
        pid_file = NamedTemporaryFile(delete=False)
        # Close it so its available for the other command
        pid_file.close()

        try:
            call_command('notifymail', daemon=True, pid=pid_file.name, no_sys_exit=False)
        except SystemExit:
            # It's normal for this command to exit
            pass

        pid = open(pid_file.name, 'r').read()
        os.unlink(pid_file.name)

        # Give it a second to start
        time.sleep(1)

        os.kill(int(pid), signal.SIGTERM)

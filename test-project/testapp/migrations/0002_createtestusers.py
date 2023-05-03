from django.db import migrations
from testapp.models import NOTIFICATION_TEST_KEY

from django_nyt.utils import subscribe

FIXTURES = (
    ("bob", "bob@example.com"),
    ("alice", "alice@example.com"),
    ("frank", ""),
)


def create_users(apps, schema_editor):
    from django.contrib.auth import get_user_model

    user_model = get_user_model()

    for username, email in FIXTURES:
        user = user_model.objects.create(
            username=username,
            email=email,
            is_active=True,
        )
        from django_nyt.models import Settings

        settings = Settings.get_default_setting(user)
        subscribe(settings, NOTIFICATION_TEST_KEY)


def remove_users(apps, schema_editor):
    user_model = apps.get_model("auth", "User")

    user_model.objects.filter(username__in=[entry[0] for entry in FIXTURES]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("testapp", "0001_initial"),
    ]

    operations = [migrations.RunPython(create_users, reverse_code=remove_users)]

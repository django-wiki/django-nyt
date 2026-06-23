from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("django_nyt", "0010_settings_created_settings_modified_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="settings",
            name="interval",
            field=models.SmallIntegerField(
                choices=[
                    (-1, "never"),
                    (0, "instantly"),
                    (1380, "daily"),
                    (9660, "weekly"),
                ],
                default=0,
                help_text="interval in minutes (0=instant, 60=notify once per hour)",
                verbose_name="interval",
            ),
        ),
    ]

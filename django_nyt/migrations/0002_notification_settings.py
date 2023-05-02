from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("django_nyt", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Settings",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        verbose_name="ID",
                        serialize=False,
                        primary_key=True,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        to_field="id",
                        to=settings.AUTH_USER_MODEL,
                        on_delete=models.CASCADE,
                    ),
                ),
                (
                    "interval",
                    models.SmallIntegerField(
                        choices=[(0, "instantly"), (1380, "daily"), (9660, "weekly")],
                        default=0,
                        verbose_name="interval",
                    ),
                ),
            ],
            options={
                "verbose_name": "settings",
                "db_table": "nyt_settings",
                "verbose_name_plural": "settings",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="Notification",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        verbose_name="ID",
                        serialize=False,
                        primary_key=True,
                    ),
                ),
                ("message", models.TextField()),
                (
                    "url",
                    models.CharField(
                        verbose_name="link for notification",
                        null=True,
                        max_length=200,
                        blank=True,
                    ),
                ),
                ("is_viewed", models.BooleanField(default=False)),
                ("is_emailed", models.BooleanField(default=False)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "occurrences",
                    models.PositiveIntegerField(
                        help_text="If the same notification was fired multiple times with no intermediate notifications",
                        default=1,
                        verbose_name="occurrences",
                    ),
                ),
            ],
            options={
                "verbose_name": "notification",
                "db_table": "nyt_notification",
                "ordering": ("-id",),
                "verbose_name_plural": "notifications",
            },
            bases=(models.Model,),
        ),
    ]

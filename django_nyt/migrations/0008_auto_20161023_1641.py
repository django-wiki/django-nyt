import django.db.models.deletion
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("django_nyt", "0007_add_modified_and_default_settings"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notification",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="nyt_notifications",
                to=settings.AUTH_USER_MODEL,
                verbose_name="user",
            ),
        ),
        migrations.AlterField(
            model_name="notificationtype",
            name="content_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="contenttypes.ContentType",
            ),
        ),
        migrations.AlterField(
            model_name="settings",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="nyt_settings",
                to=settings.AUTH_USER_MODEL,
                verbose_name="user",
            ),
        ),
    ]

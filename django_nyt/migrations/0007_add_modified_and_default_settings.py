from django.db import migrations, models
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ('django_nyt', '0006_auto_20141229_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=timezone.now()),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='is_default',
            field=models.BooleanField(default=False, verbose_name='Default for new subscriptions'),
        ),
    ]

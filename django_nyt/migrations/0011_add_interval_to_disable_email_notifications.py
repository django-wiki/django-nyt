from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_nyt', '0010_settings_created_settings_modified_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='interval',
            field=models.SmallIntegerField(default=0, verbose_name='interval', choices=[(-1, 'never'), (0, 'instantly'), (1380, 'daily'), (9660, 'weekly')]),
        ),
    ]

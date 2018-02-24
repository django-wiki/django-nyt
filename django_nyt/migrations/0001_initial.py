from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationType',
            fields=[
                ('key',
                 models.CharField(
                     verbose_name='unique key',
                     serialize=False,
                     max_length=128,
                     primary_key=True,
                     unique=True)),
                ('label',
                 models.CharField(
                     verbose_name='verbose name',
                     null=True,
                     max_length=128,
                     blank=True)),
                ('content_type',
                 models.ForeignKey(
                     to_field='id',
                     to='contenttypes.ContentType',
                     blank=True,
                     null=True, on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'type',
                'db_table': 'nyt_notificationtype',
                            'verbose_name_plural': 'types',
            },
            bases=(
                models.Model,
            ),
        ),
    ]

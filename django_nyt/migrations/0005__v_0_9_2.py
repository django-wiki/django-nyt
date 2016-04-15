from __future__ import absolute_import
from __future__ import unicode_literals
# encoding: utf8
from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_nyt', '0004_notification_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(verbose_name='user', to_field='id', blank=True, to=settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscription',
            name='latest',
            field=models.ForeignKey(verbose_name='latest notification', to_field='id', blank=True, to='django_nyt.Notification', null=True, on_delete=models.CASCADE),
        ),
        migrations.AlterField(
            model_name='settings',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id', verbose_name='user', on_delete=models.CASCADE),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='settings',
            field=models.ForeignKey(to='django_nyt.Settings', to_field='id', verbose_name='settings', on_delete=models.CASCADE),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='notification_type',
            field=models.ForeignKey(to='django_nyt.NotificationType', to_field='key', verbose_name='notification type', on_delete=models.CASCADE),
        ),
        migrations.AlterField(
            model_name='notificationtype',
            name='label',
            field=models.CharField(max_length=128, null=True, verbose_name='optional label', blank=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='object_id',
            field=models.CharField(help_text='Leave this blank to subscribe to any kind of object', max_length=64, null=True, verbose_name='object ID', blank=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='send_emails',
            field=models.BooleanField(default=True, verbose_name='send emails'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='subscription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='subscription', to_field='id', blank=True, to='django_nyt.Subscription', null=True),
        ),
    ]

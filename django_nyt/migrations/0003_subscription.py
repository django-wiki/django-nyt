# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_nyt', '0002_notification_settings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription', fields=[
                ('id', models.AutoField(
                    auto_created=True, verbose_name='ID', serialize=False, primary_key=True)), ('settings', models.ForeignKey(
                    to_field='id', to='django_nyt.Settings')), ('notification_type', models.ForeignKey(
                    to_field='key', to='django_nyt.NotificationType')), ('object_id', models.CharField(
                    help_text='Leave this blank to subscribe to any kind of object', null=True, max_length=64, blank=True)), ('send_emails', models.BooleanField(
                    default=True)), ('latest', models.ForeignKey(
                    to_field='id', to='django_nyt.Notification', blank=True, null=True)), ], options={
                'verbose_name': 'subscription', 'db_table': 'nyt_subscription', 'verbose_name_plural': 'subscriptions', }, bases=(
                models.Model,), ), ]

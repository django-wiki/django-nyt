# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_nyt', '0005__v_0_9_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='latest',
            field=models.ForeignKey(related_name='latest_for', verbose_name='latest notification', blank=True, to='django_nyt.Notification', null=True, on_delete=models.CASCADE),
            preserve_default=True,
        ),
    ]

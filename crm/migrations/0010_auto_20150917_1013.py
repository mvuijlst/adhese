# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0009_auto_20150917_0945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='nextdate',
        ),
        migrations.AddField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(null=True, verbose_name='Date/time', blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='nextevent',
            field=models.ForeignKey(to='crm.Event', null=True, blank=True),
        ),
    ]

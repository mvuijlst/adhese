# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0020_auto_20150918_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='event',
            field=models.ForeignKey(null=True, blank=True, to='crm.Event'),
        ),
    ]

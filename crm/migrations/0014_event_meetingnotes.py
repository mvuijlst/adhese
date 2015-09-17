# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0013_auto_20150917_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='meetingnotes',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]

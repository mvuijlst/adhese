# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0016_auto_20150917_1436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='companies',
        ),
    ]

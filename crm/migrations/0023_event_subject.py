# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0022_remove_event_memo'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='subject',
            field=models.CharField(null=True, blank=True, max_length=200),
        ),
    ]

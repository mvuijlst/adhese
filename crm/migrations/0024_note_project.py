# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0023_event_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='project',
            field=models.ForeignKey(to='crm.Project', null=True, blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0021_note_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='memo',
        ),
    ]

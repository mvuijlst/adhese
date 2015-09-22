# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0027_auto_20150922_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='actionperson',
            field=models.ForeignKey(to='crm.Person', blank=True, null=True, related_name='note_actionperson'),
        ),
    ]

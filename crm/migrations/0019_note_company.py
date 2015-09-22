# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0018_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='company',
            field=models.ForeignKey(to='crm.Company', blank=True, null=True),
        ),
    ]

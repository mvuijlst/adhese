# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0025_person_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='company',
            field=models.ForeignKey(null=True, blank=True, to='crm.Company'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='person',
            field=models.ForeignKey(null=True, blank=True, to='crm.Person'),
        ),
    ]

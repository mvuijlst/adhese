# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_auto_20150916_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='companies',
            field=models.ManyToManyField(to='crm.Company'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='persons',
            field=models.ManyToManyField(to='crm.Person'),
        ),
    ]

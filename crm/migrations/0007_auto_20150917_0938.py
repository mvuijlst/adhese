# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0006_auto_20150917_0928'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='companytype',
            options={'verbose_name': 'Company type', 'verbose_name_plural': 'Company types'},
        ),
        migrations.RemoveField(
            model_name='company',
            name='email',
        ),
        migrations.RemoveField(
            model_name='company',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='person',
            name='email',
        ),
        migrations.RemoveField(
            model_name='person',
            name='phone',
        ),
        migrations.AlterField(
            model_name='contact',
            name='person',
            field=models.ForeignKey(blank=True, to='crm.Company', null=True),
        ),
    ]

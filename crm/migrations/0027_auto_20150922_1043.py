# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0026_auto_20150922_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='actiondate',
            field=models.DateField(verbose_name='Action by', null=True, blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0030_auto_20150925_1451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='parentcompany',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0015_fkmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fkmodel',
            name='relation',
        ),
        migrations.DeleteModel(
            name='FkModel',
        ),
    ]

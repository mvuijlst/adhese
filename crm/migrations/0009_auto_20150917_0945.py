# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0008_auto_20150917_0941'),
    ]

    operations = [
        migrations.RenameField(
            model_name='relation',
            old_name='relationname',
            new_name='name',
        ),
    ]

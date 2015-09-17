# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0007_auto_20150917_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='person',
            field=models.ForeignKey(to='crm.Person'),
        ),
    ]

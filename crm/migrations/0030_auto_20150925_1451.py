# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0029_company_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='notetype',
            field=models.ForeignKey(default=1, to='crm.Notetype'),
            preserve_default=False,
        ),
    ]

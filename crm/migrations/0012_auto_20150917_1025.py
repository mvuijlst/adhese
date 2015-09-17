# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0011_auto_20150917_1018'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'Companies', 'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='companytype',
            options={'verbose_name': 'Company type', 'verbose_name_plural': 'Company types', 'ordering': ['typename']},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['contacttype']},
        ),
        migrations.AlterModelOptions(
            name='contacttype',
            options={'verbose_name': 'Means of contact', 'verbose_name_plural': 'Means of contact', 'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['datetime']},
        ),
        migrations.AlterModelOptions(
            name='eventtype',
            options={'verbose_name': 'Event type', 'verbose_name_plural': 'Event types', 'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['lastname', 'firstname']},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='relation',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='project',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]

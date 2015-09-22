# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0017_remove_event_companies'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Date/time')),
                ('note', models.TextField()),
                ('person', models.ForeignKey(null=True, blank=True, to='crm.Person')),
            ],
            options={
                'ordering': ['datetime'],
            },
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('address', models.TextField(null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.AddField(
            model_name='person',
            name='company',
            field=models.ForeignKey(null=True, to='crm.Company', blank=True),
        ),
    ]

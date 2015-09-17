# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0010_auto_20150917_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('memo', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='project',
            field=models.ForeignKey(null=True, blank=True, to='crm.Project'),
        ),
    ]

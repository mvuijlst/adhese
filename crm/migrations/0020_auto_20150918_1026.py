# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0019_note_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notetype',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('icon', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='note',
            name='actiondate',
            field=models.DateTimeField(verbose_name='Action by', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='note',
            name='notetype',
            field=models.ForeignKey(to='crm.Notetype', null=True, blank=True),
        ),
    ]

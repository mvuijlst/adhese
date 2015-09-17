# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(verbose_name='contact date')),
                ('nextdate', models.DateTimeField(verbose_name='next date')),
            ],
        ),
        migrations.CreateModel(
            name='Contacttype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('typename', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=150)),
                ('lastname', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='persons',
            field=models.ManyToManyField(to='crm.Person'),
        ),
        migrations.AddField(
            model_name='contact',
            name='typename',
            field=models.ForeignKey(to='crm.Contacttype'),
        ),
    ]

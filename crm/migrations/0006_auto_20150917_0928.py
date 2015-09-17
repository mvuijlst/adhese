# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_auto_20150917_0916'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('contactdata', models.CharField(max_length=200)),
                ('remark', models.CharField(blank=True, max_length=150, null=True)),
                ('valid', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Eventtype',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Event types',
                'verbose_name': 'Event type',
            },
        ),
        migrations.RemoveField(
            model_name='contactmeanspeople',
            name='person',
        ),
        migrations.DeleteModel(
            name='Contactmeanstype',
        ),
        migrations.AlterModelOptions(
            name='contacttype',
            options={'verbose_name_plural': 'Means of contact', 'verbose_name': 'Means of contact'},
        ),
        migrations.RemoveField(
            model_name='contacttype',
            name='typename',
        ),
        migrations.RemoveField(
            model_name='event',
            name='typename',
        ),
        migrations.AddField(
            model_name='contacttype',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contacttype',
            name='template',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ContactmeansPeople',
        ),
        migrations.AddField(
            model_name='contact',
            name='contacttype',
            field=models.ForeignKey(to='crm.Contacttype'),
        ),
        migrations.AddField(
            model_name='contact',
            name='person',
            field=models.ForeignKey(to='crm.Person'),
        ),
        migrations.AddField(
            model_name='event',
            name='eventtype',
            field=models.ForeignKey(blank=True, to='crm.Eventtype', null=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20150916_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='memo',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateField(verbose_name='contact date', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='nextdate',
            field=models.DateTimeField(verbose_name='next date', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='persons',
            field=models.ManyToManyField(to='crm.Person', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='typename',
            field=models.ForeignKey(to='crm.Contacttype', blank=True, null=True),
        ),
    ]

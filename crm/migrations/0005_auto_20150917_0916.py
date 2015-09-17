# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_auto_20150917_0849'),
    ]

    operations = [
        migrations.CreateModel(
            name='Companytype',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('typename', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ContactmeansPeople',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contactmeanstype',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('template', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Means of contact',
                'verbose_name_plural': 'Means of contact',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('date', models.DateField(verbose_name='contact date', null=True, blank=True)),
                ('memo', models.TextField(null=True, blank=True)),
                ('nextdate', models.DateTimeField(verbose_name='next date', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('relationname', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='contact',
            name='companies',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='persons',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='typename',
        ),
        migrations.AddField(
            model_name='company',
            name='email',
            field=models.CharField(null=True, max_length=150, blank=True),
        ),
        migrations.AddField(
            model_name='company',
            name='parentcompany',
            field=models.ForeignKey(null=True, blank=True, to='crm.Company'),
        ),
        migrations.AddField(
            model_name='company',
            name='phone',
            field=models.CharField(null=True, max_length=150, blank=True),
        ),
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.CharField(null=True, max_length=150, blank=True),
        ),
        migrations.AddField(
            model_name='person',
            name='function',
            field=models.CharField(null=True, max_length=150, blank=True),
        ),
        migrations.AddField(
            model_name='person',
            name='phone',
            field=models.CharField(null=True, max_length=150, blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='firstname',
            field=models.CharField(null=True, max_length=150, blank=True),
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.AddField(
            model_name='event',
            name='companies',
            field=models.ManyToManyField(to='crm.Company'),
        ),
        migrations.AddField(
            model_name='event',
            name='persons',
            field=models.ManyToManyField(to='crm.Person'),
        ),
        migrations.AddField(
            model_name='event',
            name='typename',
            field=models.ForeignKey(null=True, blank=True, to='crm.Contacttype'),
        ),
        migrations.AddField(
            model_name='contactmeanspeople',
            name='person',
            field=models.ForeignKey(to='crm.Person'),
        ),
        migrations.AddField(
            model_name='company',
            name='relation',
            field=models.ForeignKey(null=True, blank=True, to='crm.Relation'),
        ),
        migrations.AddField(
            model_name='company',
            name='typename',
            field=models.ForeignKey(null=True, blank=True, to='crm.Companytype'),
        ),
    ]

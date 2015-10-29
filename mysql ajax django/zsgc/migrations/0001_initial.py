# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe5\x91\x98\xe5\xb7\xa5\xe5\x90\x8d\xe5\xad\x97')),
                ('age', models.IntegerField(verbose_name=b'\xe5\xb9\xb4\xe9\xbe\x84')),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': '\u5458\u5de5',
                'verbose_name_plural': '\u5458\u5de5',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('emp_name', models.CharField(max_length=20, verbose_name=b'\xe5\x91\x98\xe5\xb7\xa5\xe5\x90\x8d\xe5\xad\x97')),
                ('emp_num', models.IntegerField(default=0, verbose_name=b'\xe5\x91\x98\xe5\xb7\xa5\xe7\xbc\x96\xe5\x8f\xb7')),
                ('employee', models.ForeignKey(to='zsgc.Employee')),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': '\u5de5\u4f5c',
                'verbose_name_plural': '\u5de5\u4f5c',
            },
        ),
    ]

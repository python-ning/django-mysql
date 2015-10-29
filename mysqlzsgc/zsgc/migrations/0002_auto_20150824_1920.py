# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zsgc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='emp_name',
            field=models.CharField(max_length=50, verbose_name=b'\xe5\xb7\xa5\xe4\xbd\x9c'),
        ),
    ]

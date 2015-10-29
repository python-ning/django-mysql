# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zsgc', '0002_auto_20150824_1920'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='emp_name',
            new_name='emp_job',
        ),
    ]

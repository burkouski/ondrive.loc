# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0008_auto_20150718_1922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autoservice',
            name='holiday',
        ),
        migrations.RemoveField(
            model_name='carwash',
            name='holiday',
        ),
        migrations.RemoveField(
            model_name='tireservice',
            name='holiday',
        ),
    ]

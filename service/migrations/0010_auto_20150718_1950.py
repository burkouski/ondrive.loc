# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0009_auto_20150718_1943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autoservice',
            name='is_moderate',
        ),
        migrations.RemoveField(
            model_name='carwash',
            name='is_moderate',
        ),
        migrations.RemoveField(
            model_name='tireservice',
            name='is_moderate',
        ),
    ]

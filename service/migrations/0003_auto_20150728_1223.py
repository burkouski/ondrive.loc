# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20150728_1219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autoservice',
            name='building',
        ),
        migrations.RemoveField(
            model_name='autoservice',
            name='city',
        ),
        migrations.RemoveField(
            model_name='carwash',
            name='building',
        ),
        migrations.RemoveField(
            model_name='carwash',
            name='city',
        ),
        migrations.RemoveField(
            model_name='tireservice',
            name='building',
        ),
        migrations.RemoveField(
            model_name='tireservice',
            name='city',
        ),
    ]

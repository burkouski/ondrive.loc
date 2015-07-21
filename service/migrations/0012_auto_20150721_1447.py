# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0011_auto_20150718_1950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autoservice',
            name='break_time_end',
        ),
        migrations.RemoveField(
            model_name='autoservice',
            name='break_time_start',
        ),
        migrations.RemoveField(
            model_name='autoservice',
            name='holiday_time_end',
        ),
        migrations.RemoveField(
            model_name='autoservice',
            name='holiday_time_start',
        ),
        migrations.RemoveField(
            model_name='autoservice',
            name='work_end',
        ),
        migrations.RemoveField(
            model_name='autoservice',
            name='work_start',
        ),
        migrations.RemoveField(
            model_name='carwash',
            name='break_time_end',
        ),
        migrations.RemoveField(
            model_name='carwash',
            name='break_time_start',
        ),
        migrations.RemoveField(
            model_name='carwash',
            name='holiday_time_end',
        ),
        migrations.RemoveField(
            model_name='carwash',
            name='holiday_time_start',
        ),
        migrations.RemoveField(
            model_name='carwash',
            name='work_end',
        ),
        migrations.RemoveField(
            model_name='carwash',
            name='work_start',
        ),
        migrations.RemoveField(
            model_name='tireservice',
            name='break_time_end',
        ),
        migrations.RemoveField(
            model_name='tireservice',
            name='break_time_start',
        ),
        migrations.RemoveField(
            model_name='tireservice',
            name='holiday_time_end',
        ),
        migrations.RemoveField(
            model_name='tireservice',
            name='holiday_time_start',
        ),
        migrations.RemoveField(
            model_name='tireservice',
            name='work_end',
        ),
        migrations.RemoveField(
            model_name='tireservice',
            name='work_start',
        ),
    ]

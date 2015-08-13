# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0009_auto_20150813_1524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autoservice',
            name='repair_work',
        ),
        migrations.AddField(
            model_name='autoservice',
            name='repairwork',
            field=models.ManyToManyField(related_name='repairwork', verbose_name='\u0420\u0435\u043c\u043e\u043d\u0442', to='service.RepairWork', blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0010_auto_20150813_1636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autoservice',
            name='repairwork',
        ),
        migrations.AddField(
            model_name='autoservice',
            name='repair_work',
            field=models.ManyToManyField(related_name='repair_work', verbose_name='\u0420\u0435\u043c\u043e\u043d\u0442', to='service.RepairWork', blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0010_auto_20150718_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='autoservice',
            name='is_moderate',
            field=models.BooleanField(default=False, verbose_name='\u0412\u044b\u0432\u043e\u0434\u0438\u0442\u044c \u0432 \u0442\u043e\u043f \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439?'),
        ),
        migrations.AddField(
            model_name='carwash',
            name='is_moderate',
            field=models.BooleanField(default=False, verbose_name='\u0412\u044b\u0432\u043e\u0434\u0438\u0442\u044c \u0432 \u0442\u043e\u043f \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439?'),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='is_moderate',
            field=models.BooleanField(default=False, verbose_name='\u0412\u044b\u0432\u043e\u0434\u0438\u0442\u044c \u0432 \u0442\u043e\u043f \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439?'),
        ),
    ]

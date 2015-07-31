# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_auto_20150728_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='autoservice',
            name='building',
            field=models.CharField(max_length=200, verbose_name='\u0414\u043e\u043c', blank=True),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='city',
            field=models.CharField(max_length=200, verbose_name='\u0413\u043e\u0440\u043e\u0434', blank=True),
        ),
        migrations.AddField(
            model_name='carwash',
            name='building',
            field=models.CharField(max_length=200, verbose_name='\u0414\u043e\u043c', blank=True),
        ),
        migrations.AddField(
            model_name='carwash',
            name='city',
            field=models.CharField(max_length=200, verbose_name='\u0413\u043e\u0440\u043e\u0434', blank=True),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='building',
            field=models.CharField(max_length=200, verbose_name='\u0414\u043e\u043c', blank=True),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='city',
            field=models.CharField(max_length=200, verbose_name='\u0413\u043e\u0440\u043e\u0434', blank=True),
        ),
    ]

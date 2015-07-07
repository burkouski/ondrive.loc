# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0007_auto_20150707_1632'),
        ('service', '0010_auto_20150701_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='autoservice',
            name='owner',
            field=models.ForeignKey(default=None, to='myauth.UserProfile'),
        ),
        migrations.AddField(
            model_name='carwash',
            name='owner',
            field=models.ForeignKey(default=None, to='myauth.UserProfile'),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='owner',
            field=models.ForeignKey(default=None, to='myauth.UserProfile'),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='phone_city',
            field=models.CharField(max_length=20, verbose_name='\u0413\u043e\u0440\u043e\u0434\u0441\u043a\u043e\u0439', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='phone_city2',
            field=models.CharField(max_length=20, verbose_name='\u0432\u0442\u043e\u0440\u043e\u0439 \u0413\u043e\u0440\u043e\u0434\u0441\u043a\u043e\u0439', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='phone_life2',
            field=models.CharField(max_length=20, verbose_name='\u0432\u0442\u043e\u0440\u043e\u0439 Life', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='phone_mts',
            field=models.CharField(max_length=20, verbose_name='\u041c\u0422\u0421', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='phone_mts2',
            field=models.CharField(max_length=10, verbose_name='\u0432\u0442\u043e\u0440\u043e\u0439 \u041c\u0422\u0421', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='work_end',
            field=models.TimeField(null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u0440\u0430\u0431\u043e\u0442\u044b', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='work_start',
            field=models.TimeField(null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0440\u0430\u0431\u043e\u0442\u044b', blank=True),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='phone_city',
            field=models.CharField(max_length=20, verbose_name='\u0413\u043e\u0440\u043e\u0434\u0441\u043a\u043e\u0439', blank=True),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='phone_city2',
            field=models.CharField(max_length=20, verbose_name='\u0432\u0442\u043e\u0440\u043e\u0439 \u0413\u043e\u0440\u043e\u0434\u0441\u043a\u043e\u0439', blank=True),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='phone_life2',
            field=models.CharField(max_length=20, verbose_name='\u0432\u0442\u043e\u0440\u043e\u0439 Life', blank=True),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='phone_mts',
            field=models.CharField(max_length=20, verbose_name='\u041c\u0422\u0421', blank=True),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='phone_mts2',
            field=models.CharField(max_length=10, verbose_name='\u0432\u0442\u043e\u0440\u043e\u0439 \u041c\u0422\u0421', blank=True),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='work_end',
            field=models.TimeField(null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u0440\u0430\u0431\u043e\u0442\u044b', blank=True),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='work_start',
            field=models.TimeField(null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0440\u0430\u0431\u043e\u0442\u044b', blank=True),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='phone_city',
            field=models.CharField(max_length=20, verbose_name='\u0413\u043e\u0440\u043e\u0434\u0441\u043a\u043e\u0439', blank=True),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='phone_city2',
            field=models.CharField(max_length=20, verbose_name='\u0432\u0442\u043e\u0440\u043e\u0439 \u0413\u043e\u0440\u043e\u0434\u0441\u043a\u043e\u0439', blank=True),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='phone_life2',
            field=models.CharField(max_length=20, verbose_name='\u0432\u0442\u043e\u0440\u043e\u0439 Life', blank=True),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='phone_mts',
            field=models.CharField(max_length=20, verbose_name='\u041c\u0422\u0421', blank=True),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='phone_mts2',
            field=models.CharField(max_length=10, verbose_name='\u0432\u0442\u043e\u0440\u043e\u0439 \u041c\u0422\u0421', blank=True),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='work_end',
            field=models.TimeField(null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u0440\u0430\u0431\u043e\u0442\u044b', blank=True),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='work_start',
            field=models.TimeField(null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0440\u0430\u0431\u043e\u0442\u044b', blank=True),
        ),
    ]

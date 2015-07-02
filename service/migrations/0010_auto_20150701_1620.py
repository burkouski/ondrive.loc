# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0009_auto_20150701_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autoservice',
            name='friday',
            field=models.CharField(default=b'wd', max_length=2, verbose_name=b'\xd0\x9f\xd1\x8f\xd1\x82\xd0\xbd\xd0\xb8\xd1\x86\xd0\xb0', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')]),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='monday',
            field=models.CharField(default=b'wd', max_length=2, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbd\xd0\xb5\xd0\xb4\xd0\xb5\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xb8\xd0\xba', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')]),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='saturday',
            field=models.CharField(default=b'wd', max_length=2, verbose_name=b'\xd0\xa1\xd1\x83\xd0\xb1\xd0\xb1\xd0\xbe\xd1\x82\xd0\xb0', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')]),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='sunday',
            field=models.CharField(default=b'wd', max_length=2, verbose_name=b'\xd0\x92\xd0\xbe\xd1\x81\xd0\xba\xd1\x80\xd0\xb5\xd1\x81\xd0\xb5\xd0\xbd\xd1\x8c\xd0\xb5', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')]),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='thursday',
            field=models.CharField(default=b'wd', max_length=2, verbose_name=b'\xd0\xa7\xd0\xb5\xd1\x82\xd0\xb2\xd0\xb5\xd1\x80\xd0\xb3', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')]),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='tuesday',
            field=models.CharField(default=b'wd', max_length=2, verbose_name=b'\xd0\x92\xd1\x82\xd0\xbe\xd1\x80\xd0\xbd\xd0\xb8\xd0\xba', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')]),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='wednesday',
            field=models.CharField(default=b'wd', max_length=2, verbose_name=b'\xd0\xa1\xd1\x80\xd0\xb5\xd0\xb4\xd0\xb0', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')]),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='friday',
            field=models.CharField(default=b'wd', max_length=2, verbose_name=b'\xd0\x9f\xd1\x8f\xd1\x82\xd0\xbd\xd0\xb8\xd1\x86\xd0\xb0', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')]),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='monday',
            field=models.CharField(default=b'wd', max_length=2, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbd\xd0\xb5\xd0\xb4\xd0\xb5\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xb8\xd0\xba', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')]),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='saturday',
            field=models.CharField(default=b'wd', max_length=2, verbose_name=b'\xd0\xa1\xd1\x83\xd0\xb1\xd0\xb1\xd0\xbe\xd1\x82\xd0\xb0', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')]),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='sunday',
            field=models.CharField(default=b'wd', max_length=2, verbose_name=b'\xd0\x92\xd0\xbe\xd1\x81\xd0\xba\xd1\x80\xd0\xb5\xd1\x81\xd0\xb5\xd0\xbd\xd1\x8c\xd0\xb5', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')]),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='thursday',
            field=models.CharField(default=b'wd', max_length=2, verbose_name=b'\xd0\xa7\xd0\xb5\xd1\x82\xd0\xb2\xd0\xb5\xd1\x80\xd0\xb3', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')]),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='tuesday',
            field=models.CharField(default=b'wd', max_length=2, verbose_name=b'\xd0\x92\xd1\x82\xd0\xbe\xd1\x80\xd0\xbd\xd0\xb8\xd0\xba', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')]),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='wednesday',
            field=models.CharField(default=b'wd', max_length=2, verbose_name=b'\xd0\xa1\xd1\x80\xd0\xb5\xd0\xb4\xd0\xb0', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')]),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='friday',
            field=models.CharField(default=b'wd', max_length=2, verbose_name=b'\xd0\x9f\xd1\x8f\xd1\x82\xd0\xbd\xd0\xb8\xd1\x86\xd0\xb0', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')]),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='monday',
            field=models.CharField(default=b'wd', max_length=2, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbd\xd0\xb5\xd0\xb4\xd0\xb5\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xb8\xd0\xba', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')]),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='saturday',
            field=models.CharField(default=b'wd', max_length=2, verbose_name=b'\xd0\xa1\xd1\x83\xd0\xb1\xd0\xb1\xd0\xbe\xd1\x82\xd0\xb0', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')]),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='sunday',
            field=models.CharField(default=b'wd', max_length=2, verbose_name=b'\xd0\x92\xd0\xbe\xd1\x81\xd0\xba\xd1\x80\xd0\xb5\xd1\x81\xd0\xb5\xd0\xbd\xd1\x8c\xd0\xb5', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')]),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='thursday',
            field=models.CharField(default=b'wd', max_length=2, verbose_name=b'\xd0\xa7\xd0\xb5\xd1\x82\xd0\xb2\xd0\xb5\xd1\x80\xd0\xb3', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')]),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='tuesday',
            field=models.CharField(default=b'wd', max_length=2, verbose_name=b'\xd0\x92\xd1\x82\xd0\xbe\xd1\x80\xd0\xbd\xd0\xb8\xd0\xba', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')]),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='wednesday',
            field=models.CharField(default=b'wd', max_length=2, verbose_name=b'\xd0\xa1\xd1\x80\xd0\xb5\xd0\xb4\xd0\xb0', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')]),
        ),
    ]

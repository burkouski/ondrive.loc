# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0008_auto_20150813_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='addservices',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0444\u0438\u043b\u044c\u0442\u0440\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='addservices',
            name='lastmod',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='addwork',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0444\u0438\u043b\u044c\u0442\u0440\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='addwork',
            name='lastmod',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='lastmod',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='carwash',
            name='lastmod',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='carwashservices',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0444\u0438\u043b\u044c\u0442\u0440\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='carwashservices',
            name='lastmod',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='diagwork',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0444\u0438\u043b\u044c\u0442\u0440\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='diagwork',
            name='lastmod',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='discwork',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0444\u0438\u043b\u044c\u0442\u0440\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='discwork',
            name='lastmod',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='repairwork',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0444\u0438\u043b\u044c\u0442\u0440\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='repairwork',
            name='lastmod',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='servwork',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0444\u0438\u043b\u044c\u0442\u0440\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='servwork',
            name='lastmod',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='specializationwork',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0444\u0438\u043b\u044c\u0442\u0440\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='specializationwork',
            name='lastmod',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='lastmod',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='tirework',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0444\u0438\u043b\u044c\u0442\u0440\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='tirework',
            name='lastmod',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='typecarwash',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0444\u0438\u043b\u044c\u0442\u0440\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='typecarwash',
            name='lastmod',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='typevehicle',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0444\u0438\u043b\u044c\u0442\u0440\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='typevehicle',
            name='lastmod',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]

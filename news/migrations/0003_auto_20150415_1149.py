# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20150415_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание категории'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='meta_description',
            field=models.TextField(blank=True, verbose_name='Description'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='meta_keywords',
            field=models.TextField(blank=True, verbose_name='Keywords'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='title',
            field=models.CharField(blank=True, max_length=200, verbose_name='title страницы'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='alias',
            field=models.SlugField(blank=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='meta_description',
            field=models.TextField(blank=True, verbose_name='Description'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='meta_keywords',
            field=models.TextField(blank=True, verbose_name='Keywords'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, max_length=200, verbose_name='title страницы'),
            preserve_default=True,
        ),
    ]

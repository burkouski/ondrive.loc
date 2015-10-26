# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_post_lastmod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=200, verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438', blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=200, verbose_name='title \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b', blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=200, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0441\u0442\u0430\u0442\u044c\u0438'),
        ),
        migrations.AlterField(
            model_name='post',
            name='preview',
            field=models.TextField(verbose_name='\u0412\u0441\u0442\u0443\u043f\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442'),
        ),
        migrations.AlterField(
            model_name='post',
            name='preview_img',
            field=models.ImageField(upload_to=b'', verbose_name='\u041f\u0440\u0435\u0432\u044c\u044e \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name='\u041f\u043e\u043b\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, verbose_name='title \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b', blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0432\u0438\u0434\u0435\u043e', blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='views',
            field=models.IntegerField(verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u043e\u0432'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20150510_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='name',
            field=models.CharField(max_length=200, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b'),
        ),
        migrations.AlterField(
            model_name='page',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b'),
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=200, verbose_name='title \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b', blank=True),
        ),
    ]

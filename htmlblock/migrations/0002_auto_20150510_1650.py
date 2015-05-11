# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('htmlblock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='htmlblock',
            name='label',
            field=models.CharField(max_length=200, verbose_name='\u041d\u0430 \u0437\u0432\u0430\u043d\u0438\u0435 \u0434\u043b\u044f \u0438\u043d\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u0438'),
        ),
        migrations.AlterField(
            model_name='htmlblock',
            name='name',
            field=models.CharField(max_length=200, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0431\u043b\u043e\u043a\u0430'),
        ),
        migrations.AlterField(
            model_name='htmlblock',
            name='name_align',
            field=models.CharField(max_length=100, choices=[(b'text-left', '\u0421\u043b\u0435\u0432\u0430'), (b'text-right', '\u0421\u043f\u0440\u0430\u0432\u0430'), (b'text-center', '\u041f\u043e \u0446\u0435\u043d\u0442\u0440\u0443')]),
        ),
        migrations.AlterField(
            model_name='htmlblock',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0431\u043b\u043e\u043a\u0430'),
        ),
        migrations.AlterField(
            model_name='htmlblock',
            name='text_align',
            field=models.CharField(max_length=100, choices=[(b'text-left', '\u0421\u043b\u0435\u0432\u0430'), (b'text-right', '\u0421\u043f\u0440\u0430\u0432\u0430'), (b'text-center', '\u041f\u043e \u0446\u0435\u043d\u0442\u0440\u0443')]),
        ),
    ]

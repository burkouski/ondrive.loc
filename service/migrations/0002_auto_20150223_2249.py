# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autoservice',
            name='friday',
            field=models.BooleanField(verbose_name='Пятница', default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='monday',
            field=models.BooleanField(verbose_name='Понедельник', default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='saturday',
            field=models.BooleanField(verbose_name='Суббота', default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='sunday',
            field=models.BooleanField(verbose_name='Воскресенье', default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='thursday',
            field=models.BooleanField(verbose_name='Четверг', default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='tuesday',
            field=models.BooleanField(verbose_name='Вторник', default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='wednesday',
            field=models.BooleanField(verbose_name='Среда', default=None),
            preserve_default=True,
        ),
    ]

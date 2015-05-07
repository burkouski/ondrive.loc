# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20150415_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='meta_description',
            field=models.TextField(verbose_name='meta description', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='meta_keywords',
            field=models.TextField(verbose_name='meta keywords', blank=True),
            preserve_default=True,
        ),
    ]

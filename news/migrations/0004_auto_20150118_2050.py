# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20150118_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_class',
            field=models.CharField(choices=[('', '1 колонка'), ('post-preview_medium', '2 колонки'), ('post-preview_huge', '3 колонки')], max_length=100, default=''),
            preserve_default=True,
        ),
    ]

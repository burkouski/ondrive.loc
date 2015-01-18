# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_post_post_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_class',
            field=models.CharField(choices=[('', '1 колонка'), ('post-preview_medium', '2 колонки'), ('post-preview_huge', '3 колонки')], default='', max_length=1),
            preserve_default=True,
        ),
    ]

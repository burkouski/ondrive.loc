# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_post_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.CharField(blank=True, null=True, max_length=1000, verbose_name='Ссылка на видео'),
            preserve_default=True,
        ),
    ]

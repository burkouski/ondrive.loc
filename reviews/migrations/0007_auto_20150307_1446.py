# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_auto_20150223_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='pub_date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата публикации'),
            preserve_default=True,
        ),
    ]

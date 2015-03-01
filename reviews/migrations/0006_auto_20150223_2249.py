# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_review_is_moderate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='is_moderate',
            field=models.NullBooleanField(default=None, verbose_name='Прошел модерацию?'),
            preserve_default=True,
        ),
    ]

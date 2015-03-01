# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_remove_review_is_moderate'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='is_moderate',
            field=models.BooleanField(default=None, verbose_name='Прошел модерацию?'),
            preserve_default=True,
        ),
    ]

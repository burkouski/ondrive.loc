# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_review_is_moderate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='is_moderate',
        ),
    ]

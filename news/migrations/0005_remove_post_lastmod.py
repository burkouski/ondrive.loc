# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20150813_1256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='lastmod',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_auto_20150813_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autoservice',
            name='lastmod',
        ),
        migrations.RemoveField(
            model_name='carwash',
            name='lastmod',
        ),
        migrations.RemoveField(
            model_name='tireservice',
            name='lastmod',
        ),
    ]

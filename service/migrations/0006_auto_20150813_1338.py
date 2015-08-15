# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_auto_20150813_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='autoservice',
            name='lastmod',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='carwash',
            name='lastmod',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='lastmod',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]

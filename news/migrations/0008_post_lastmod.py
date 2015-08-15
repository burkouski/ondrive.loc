# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20150813_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='lastmod',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]

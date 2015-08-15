# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_post_lastmod'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='lastmod',
        ),
        migrations.AddField(
            model_name='category',
            name='lastmod',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]

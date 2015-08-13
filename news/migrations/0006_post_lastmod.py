# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_remove_post_lastmod'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='lastmod',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]

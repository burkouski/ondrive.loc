# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_remove_post_change_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='change_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]

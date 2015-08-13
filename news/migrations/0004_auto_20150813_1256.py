# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_post_change_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='change_date',
            new_name='lastmod',
        ),
    ]

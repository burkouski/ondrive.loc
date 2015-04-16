# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.RemoveField(
            model_name='category',
            name='meta_description',
        ),
        migrations.RemoveField(
            model_name='category',
            name='meta_keywords',
        ),
        migrations.RemoveField(
            model_name='category',
            name='title',
        ),
        migrations.RemoveField(
            model_name='post',
            name='alias',
        ),
        migrations.RemoveField(
            model_name='post',
            name='meta_description',
        ),
        migrations.RemoveField(
            model_name='post',
            name='meta_keywords',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]

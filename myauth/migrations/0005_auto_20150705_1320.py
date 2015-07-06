# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0004_auto_20150414_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='sur_name',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]

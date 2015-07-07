# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0011_auto_20150707_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autoservice',
            name='owner',
            field=models.ForeignKey(default=None, blank=True, to='myauth.UserProfile'),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='owner',
            field=models.ForeignKey(default=None, blank=True, to='myauth.UserProfile'),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='owner',
            field=models.ForeignKey(default=None, blank=True, to='myauth.UserProfile'),
        ),
    ]

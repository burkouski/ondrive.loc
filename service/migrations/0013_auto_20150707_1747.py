# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0012_auto_20150707_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autoservice',
            name='owner',
            field=models.ForeignKey(to='myauth.UserProfile'),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='owner',
            field=models.ForeignKey(to='myauth.UserProfile'),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='owner',
            field=models.ForeignKey(to='myauth.UserProfile'),
        ),
    ]

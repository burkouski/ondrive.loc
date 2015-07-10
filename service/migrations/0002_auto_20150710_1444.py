# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0001_initial'),
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='autoservice',
            name='owner',
            field=models.ForeignKey(default=b'85', to='myauth.UserProfile'),
        ),
        migrations.AddField(
            model_name='carwash',
            name='owner',
            field=models.ForeignKey(default=b'85', to='myauth.UserProfile'),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='owner',
            field=models.ForeignKey(default=b'85', to='myauth.UserProfile'),
        ),
    ]

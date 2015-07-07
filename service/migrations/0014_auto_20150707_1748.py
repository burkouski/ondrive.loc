# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0013_auto_20150707_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autoservice',
            name='meta_description',
            field=models.TextField(null=True, verbose_name=b'Description', blank=True),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='meta_description',
            field=models.TextField(null=True, verbose_name=b'Description', blank=True),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='meta_description',
            field=models.TextField(null=True, verbose_name=b'Description', blank=True),
        ),
    ]

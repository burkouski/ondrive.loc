# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_auto_20150307_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='author',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x90\xd0\xb2\xd1\x82\xd0\xbe\xd1\x80'),
        ),
        migrations.AlterField(
            model_name='review',
            name='is_moderate',
            field=models.NullBooleanField(default=None, verbose_name=b'\xd0\x9f\xd1\x80\xd0\xbe\xd1\x88\xd0\xb5\xd0\xbb \xd0\xbc\xd0\xbe\xd0\xb4\xd0\xb5\xd1\x80\xd0\xb0\xd1\x86\xd0\xb8\xd1\x8e?'),
        ),
        migrations.AlterField(
            model_name='review',
            name='pub_date',
            field=models.DateField(auto_now_add=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbf\xd1\x83\xd0\xb1\xd0\xbb\xd0\xb8\xd0\xba\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.PositiveIntegerField(verbose_name=b'\xd0\xa0\xd0\xb5\xd0\xb9\xd1\x82\xd0\xb8\xd0\xbd\xd0\xb3'),
        ),
        migrations.AlterField(
            model_name='review',
            name='review',
            field=models.TextField(verbose_name=b'\xd0\x9e\xd1\x82\xd0\xb7\xd1\x8b\xd0\xb2'),
        ),
    ]

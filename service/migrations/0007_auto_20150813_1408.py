# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_auto_20150813_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='addservices',
            name='alias',
            field=models.SlugField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='addwork',
            name='alias',
            field=models.SlugField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='carwashservices',
            name='alias',
            field=models.SlugField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='diagwork',
            name='alias',
            field=models.SlugField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='discwork',
            name='alias',
            field=models.SlugField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='repairwork',
            name='alias',
            field=models.SlugField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='servwork',
            name='alias',
            field=models.SlugField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='specializationwork',
            name='alias',
            field=models.SlugField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='tirework',
            name='alias',
            field=models.SlugField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='typecarwash',
            name='alias',
            field=models.SlugField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='typevehicle',
            name='alias',
            field=models.SlugField(max_length=100, blank=True),
        ),
    ]

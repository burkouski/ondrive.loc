# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CarWash',
        ),
        migrations.DeleteModel(
            name='CarWashWork',
        ),
        migrations.DeleteModel(
            name='TireService',
        ),
        migrations.DeleteModel(
            name='TireServiceWork',
        ),
    ]

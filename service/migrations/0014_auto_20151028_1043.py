# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0013_auto_20151028_1042'),
    ]

    operations = [
        migrations.RenameField('CarWash', 'car_wash_services', 'carwash_services'),
    ]

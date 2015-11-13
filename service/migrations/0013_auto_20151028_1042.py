# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0012_auto_20151026_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carwash',
            name='car_wash_services',
            field=models.ManyToManyField(related_name='carwash_services', verbose_name='\u0423\u0441\u043b\u0443\u0433\u0438', to='service.CarWashServices', blank=True),
        ),
    ]

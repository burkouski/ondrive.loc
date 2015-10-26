# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0011_auto_20150813_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addservices',
            name='logo',
            field=models.ImageField(upload_to=b'', verbose_name='\u0438\u043a\u043e\u043d\u043a\u0430 \u0443\u0441\u043b\u0443\u0433\u0438', blank=True),
        ),
        migrations.AlterField(
            model_name='addservices',
            name='work_name',
            field=models.CharField(max_length=200, verbose_name='\u0412\u0438\u0434 \u0440\u0430\u0431\u043e\u0442\u044b'),
        ),
        migrations.AlterField(
            model_name='addwork',
            name='work_name',
            field=models.CharField(max_length=200, verbose_name='\u0412\u0438\u0434 \u0440\u0430\u0431\u043e\u0442\u044b'),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='phone_mts2',
            field=models.CharField(max_length=20, verbose_name='\u0432\u0442\u043e\u0440\u043e\u0439 \u041c\u0422\u0421', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='teaser',
            field=models.TextField(max_length=300, verbose_name='\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='add_services',
            field=models.ManyToManyField(related_name='carwash_add_services', verbose_name='\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u0443\u0441\u043b\u0443\u0433\u0438', to='service.AddServices', blank=True),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='car_wash_services',
            field=models.ManyToManyField(related_name='car_wash_services', verbose_name='\u0423\u0441\u043b\u0443\u0433\u0438', to='service.CarWashServices', blank=True),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='phone_mts2',
            field=models.CharField(max_length=20, verbose_name='\u0432\u0442\u043e\u0440\u043e\u0439 \u041c\u0422\u0421', blank=True),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='teaser',
            field=models.TextField(max_length=300, verbose_name='\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='type_carwash',
            field=models.ManyToManyField(related_name='type_carwash', verbose_name='\u0412\u0438\u0434 \u043c\u043e\u0439\u043a\u0438', to='service.TypeCarWash', blank=True),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='type_vehicle',
            field=models.ManyToManyField(related_name='type_vehicle', verbose_name='\u0412\u0438\u0434 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0430', to='service.TypeVehicle', blank=True),
        ),
        migrations.AlterField(
            model_name='carwashservices',
            name='work_name',
            field=models.CharField(max_length=200, verbose_name='\u0412\u0438\u0434 \u0440\u0430\u0431\u043e\u0442\u044b'),
        ),
        migrations.AlterField(
            model_name='diagwork',
            name='work_name',
            field=models.CharField(max_length=200, verbose_name='\u0412\u0438\u0434 \u0440\u0430\u0431\u043e\u0442\u044b'),
        ),
        migrations.AlterField(
            model_name='discwork',
            name='work_name',
            field=models.CharField(max_length=200, verbose_name='\u0412\u0438\u0434 \u0440\u0430\u0431\u043e\u0442\u044b'),
        ),
        migrations.AlterField(
            model_name='repairwork',
            name='work_name',
            field=models.CharField(max_length=200, verbose_name='\u0412\u0438\u0434 \u0440\u0430\u0431\u043e\u0442\u044b'),
        ),
        migrations.AlterField(
            model_name='servwork',
            name='work_name',
            field=models.CharField(max_length=200, verbose_name='\u0412\u0438\u0434 \u0440\u0430\u0431\u043e\u0442\u044b'),
        ),
        migrations.AlterField(
            model_name='specializationwork',
            name='logo',
            field=models.ImageField(upload_to=b'', verbose_name='\u041b\u043e\u0433\u043e\u0442\u0438\u043f \u043c\u0430\u0440\u043a\u0438', blank=True),
        ),
        migrations.AlterField(
            model_name='specializationwork',
            name='work_name',
            field=models.CharField(max_length=200, verbose_name='\u0412\u0438\u0434 \u0440\u0430\u0431\u043e\u0442\u044b'),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='add_services',
            field=models.ManyToManyField(related_name='tire_add_services', verbose_name='\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u0443\u0441\u043b\u0443\u0433\u0438', to='service.AddServices', blank=True),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='disc_work',
            field=models.ManyToManyField(related_name='disc_work', verbose_name='\u0414\u0438\u0441\u043a\u0438', to='service.DiscWork', blank=True),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='phone_mts2',
            field=models.CharField(max_length=20, verbose_name='\u0432\u0442\u043e\u0440\u043e\u0439 \u041c\u0422\u0421', blank=True),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='teaser',
            field=models.TextField(max_length=300, verbose_name='\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='tire_work',
            field=models.ManyToManyField(related_name='tire_work', verbose_name='\u0428\u0438\u043d\u044b', to='service.TireWork', blank=True),
        ),
        migrations.AlterField(
            model_name='tirework',
            name='work_name',
            field=models.CharField(max_length=200, verbose_name='\u0412\u0438\u0434 \u0440\u0430\u0431\u043e\u0442\u044b'),
        ),
        migrations.AlterField(
            model_name='typecarwash',
            name='work_name',
            field=models.CharField(max_length=200, verbose_name='\u0412\u0438\u0434 \u0440\u0430\u0431\u043e\u0442\u044b'),
        ),
        migrations.AlterField(
            model_name='typevehicle',
            name='work_name',
            field=models.CharField(max_length=200, verbose_name='\u0412\u0438\u0434 \u0440\u0430\u0431\u043e\u0442\u044b'),
        ),
    ]

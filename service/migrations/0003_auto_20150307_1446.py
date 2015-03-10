# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20150223_2249'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddServices',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('work_name', models.CharField(verbose_name='Вид работы', max_length=200)),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Дополнительные услуги',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CarWash',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Название сервиса', max_length=200)),
                ('alias', models.SlugField(max_length=100, blank=True)),
                ('teaser', models.TextField(verbose_name='Краткое описание')),
                ('address', models.CharField(verbose_name='Адрес', max_length=200)),
                ('phone_velcom', models.CharField(verbose_name='Velcom', max_length=20, blank=True)),
                ('phone_velcom2', models.CharField(verbose_name='второй Velcom', max_length=20, blank=True)),
                ('phone_mts', models.CharField(verbose_name='МТС', max_length=20, blank=True)),
                ('phone_mts2', models.CharField(verbose_name='второй МТС', max_length=10, blank=True)),
                ('phone_life', models.CharField(verbose_name='Life', max_length=20, blank=True)),
                ('phone_life2', models.CharField(verbose_name='второй Life', max_length=20, blank=True)),
                ('phone_city', models.CharField(verbose_name='Городской', max_length=20, blank=True)),
                ('phone_city2', models.CharField(verbose_name='второй Городской', max_length=20, blank=True)),
                ('work_start', models.TimeField(verbose_name='Время начала работы', blank=True, null=True)),
                ('work_end', models.TimeField(verbose_name='Время завершения работы', blank=True, null=True)),
                ('break_time_start', models.TimeField(verbose_name='Время начала обеда', blank=True, null=True)),
                ('break_time_end', models.TimeField(verbose_name='Время завершения обеда', blank=True, null=True)),
                ('holiday', models.CharField(verbose_name='Сокращенные дни', max_length=10, blank=True)),
                ('holiday_time_start', models.TimeField(verbose_name='Время начала сокращенного дня', blank=True, null=True)),
                ('holiday_time_end', models.TimeField(verbose_name='Время завершения сокращенного дня', blank=True, null=True)),
                ('monday', models.BooleanField(verbose_name='Понедельник', default=None)),
                ('tuesday', models.BooleanField(verbose_name='Вторник', default=None)),
                ('wednesday', models.BooleanField(verbose_name='Среда', default=None)),
                ('thursday', models.BooleanField(verbose_name='Четверг', default=None)),
                ('friday', models.BooleanField(verbose_name='Пятница', default=None)),
                ('saturday', models.BooleanField(verbose_name='Суббота', default=None)),
                ('sunday', models.BooleanField(verbose_name='Воскресенье', default=None)),
                ('email', models.EmailField(verbose_name='Email', max_length=75, blank=True)),
                ('site_url', models.URLField(verbose_name='Сайт', blank=True)),
                ('full_desc', ckeditor.fields.RichTextField(verbose_name='Полное описание', blank=True)),
                ('logo', models.ImageField(upload_to='', verbose_name='Логотип компании', blank=True)),
                ('is_top', models.BooleanField(verbose_name='Выводить в топ на главной?', default=None)),
                ('latitude', models.CharField(verbose_name='Широта', max_length=200, blank=True)),
                ('longitude', models.CharField(verbose_name='Долгота', max_length=200, blank=True)),
                ('title', models.CharField(verbose_name='title страницы', max_length=200, blank=True)),
                ('meta_keywords', models.TextField(verbose_name='Keywords', blank=True)),
                ('meta_description', models.TextField(verbose_name='Description', blank=True)),
                ('add_services', models.ManyToManyField(verbose_name='Дополнительные услуги', to='service.AddServices', related_name='add_services', blank=True)),
            ],
            options={
                'verbose_name': 'Автомойка',
                'verbose_name_plural': 'Автомойки',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CarWashServices',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('work_name', models.CharField(verbose_name='Вид работы', max_length=200)),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Услуги',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TypeCarWash',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('work_name', models.CharField(verbose_name='Вид работы', max_length=200)),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Вид мойки',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TypeVehicle',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('work_name', models.CharField(verbose_name='Вид работы', max_length=200)),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Вид транспорта',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='carwash',
            name='car_wash_services',
            field=models.ManyToManyField(verbose_name='Услуги', to='service.CarWashServices', related_name='car_wash_services', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='carwash',
            name='type_carwash',
            field=models.ManyToManyField(verbose_name='Вид мойки', to='service.TypeCarWash', related_name='type_carwash', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='carwash',
            name='type_vehicle',
            field=models.ManyToManyField(verbose_name='Вид транспорта', to='service.TypeVehicle', related_name='type_vehicle', blank=True),
            preserve_default=True,
        ),
    ]

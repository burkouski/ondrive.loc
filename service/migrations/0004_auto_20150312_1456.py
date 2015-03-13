# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_auto_20150307_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscWork',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('work_name', models.CharField(max_length=200, verbose_name='Вид работы')),
            ],
            options={
                'verbose_name_plural': 'Диски',
                'verbose_name': '',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TireService',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название сервиса')),
                ('alias', models.SlugField(blank=True, max_length=100)),
                ('teaser', models.TextField(verbose_name='Краткое описание')),
                ('address', models.CharField(max_length=200, verbose_name='Адрес')),
                ('phone_velcom', models.CharField(blank=True, max_length=20, verbose_name='Velcom')),
                ('phone_velcom2', models.CharField(blank=True, max_length=20, verbose_name='второй Velcom')),
                ('phone_mts', models.CharField(blank=True, max_length=20, verbose_name='МТС')),
                ('phone_mts2', models.CharField(blank=True, max_length=10, verbose_name='второй МТС')),
                ('phone_life', models.CharField(blank=True, max_length=20, verbose_name='Life')),
                ('phone_life2', models.CharField(blank=True, max_length=20, verbose_name='второй Life')),
                ('phone_city', models.CharField(blank=True, max_length=20, verbose_name='Городской')),
                ('phone_city2', models.CharField(blank=True, max_length=20, verbose_name='второй Городской')),
                ('work_start', models.TimeField(null=True, blank=True, verbose_name='Время начала работы')),
                ('work_end', models.TimeField(null=True, blank=True, verbose_name='Время завершения работы')),
                ('break_time_start', models.TimeField(null=True, blank=True, verbose_name='Время начала обеда')),
                ('break_time_end', models.TimeField(null=True, blank=True, verbose_name='Время завершения обеда')),
                ('holiday', models.CharField(blank=True, max_length=10, verbose_name='Сокращенные дни')),
                ('holiday_time_start', models.TimeField(null=True, blank=True, verbose_name='Время начала сокращенного дня')),
                ('holiday_time_end', models.TimeField(null=True, blank=True, verbose_name='Время завершения сокращенного дня')),
                ('monday', models.BooleanField(default=None, verbose_name='Понедельник')),
                ('tuesday', models.BooleanField(default=None, verbose_name='Вторник')),
                ('wednesday', models.BooleanField(default=None, verbose_name='Среда')),
                ('thursday', models.BooleanField(default=None, verbose_name='Четверг')),
                ('friday', models.BooleanField(default=None, verbose_name='Пятница')),
                ('saturday', models.BooleanField(default=None, verbose_name='Суббота')),
                ('sunday', models.BooleanField(default=None, verbose_name='Воскресенье')),
                ('email', models.EmailField(blank=True, max_length=75, verbose_name='Email')),
                ('site_url', models.URLField(blank=True, verbose_name='Сайт')),
                ('full_desc', ckeditor.fields.RichTextField(blank=True, verbose_name='Полное описание')),
                ('logo', models.ImageField(upload_to='', blank=True, verbose_name='Логотип компании')),
                ('is_top', models.BooleanField(default=None, verbose_name='Выводить в топ на главной?')),
                ('latitude', models.CharField(blank=True, max_length=200, verbose_name='Широта')),
                ('longitude', models.CharField(blank=True, max_length=200, verbose_name='Долгота')),
                ('title', models.CharField(blank=True, max_length=200, verbose_name='title страницы')),
                ('meta_keywords', models.TextField(blank=True, verbose_name='Keywords')),
                ('meta_description', models.TextField(blank=True, verbose_name='Description')),
                ('add_services', models.ManyToManyField(related_name='tire_add_services', blank=True, to='service.AddServices', verbose_name='Дополнительные услуги')),
                ('disc_work', models.ManyToManyField(related_name='disc_work', blank=True, to='service.DiscWork', verbose_name='Диски')),
            ],
            options={
                'verbose_name_plural': 'Шиномонтажи',
                'verbose_name': 'Шиномонтаж',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TireWork',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('work_name', models.CharField(max_length=200, verbose_name='Вид работы')),
            ],
            options={
                'verbose_name_plural': 'Шины',
                'verbose_name': '',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='tire_work',
            field=models.ManyToManyField(related_name='tire_work', blank=True, to='service.TireWork', verbose_name='Шины'),
            preserve_default=True,
        ),
    ]

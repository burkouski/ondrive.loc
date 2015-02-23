# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AirConditionRepairWork',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('work_name', models.CharField(max_length=200, verbose_name='Вид работы')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Кондиционер, радиаторы',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AudioAlarmRepairWork',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('work_name', models.CharField(max_length=200, verbose_name='Вид работы')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Аудио, Сигнализации',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AutoDiagWork',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('work_name', models.CharField(max_length=200, verbose_name='Вид работы')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Диагностика автомобилей',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AutoglassesRepairWork',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('work_name', models.CharField(max_length=200, verbose_name='Вид работы')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Автостекла',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AutoService',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
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
                ('work_start', models.TimeField(blank=True, verbose_name='Время начала работы', null=True)),
                ('work_end', models.TimeField(blank=True, verbose_name='Время завершения работы', null=True)),
                ('break_time_start', models.TimeField(blank=True, verbose_name='Время начала обеда', null=True)),
                ('break_time_end', models.TimeField(blank=True, verbose_name='Время завершения обеда', null=True)),
                ('holiday', models.CharField(blank=True, max_length=10, verbose_name='Сокращенные дни')),
                ('holiday_time_start', models.TimeField(blank=True, verbose_name='Время начала сокращенного дня', null=True)),
                ('holiday_time_end', models.TimeField(blank=True, verbose_name='Время завершения сокращенного дня', null=True)),
                ('monday', models.BooleanField(verbose_name='Понедельник')),
                ('tuesday', models.BooleanField(verbose_name='Вторник')),
                ('wednesday', models.BooleanField(verbose_name='Среда')),
                ('thursday', models.BooleanField(verbose_name='Четверг')),
                ('friday', models.BooleanField(verbose_name='Пятница')),
                ('saturday', models.BooleanField(verbose_name='Суббота')),
                ('sunday', models.BooleanField(verbose_name='Воскресенье')),
                ('email', models.EmailField(blank=True, max_length=75, verbose_name='Email')),
                ('site_url', models.URLField(blank=True, verbose_name='Сайт')),
                ('full_desc', ckeditor.fields.RichTextField(blank=True, verbose_name='Полное описание')),
                ('logo', models.ImageField(blank=True, verbose_name='Логотип компании', upload_to='')),
                ('is_top', models.BooleanField(verbose_name='Выводить в топ на главной?', default=None)),
                ('latitude', models.CharField(blank=True, max_length=200, verbose_name='Широта')),
                ('longitude', models.CharField(blank=True, max_length=200, verbose_name='Долгота')),
                ('title', models.CharField(blank=True, max_length=200, verbose_name='title страницы')),
                ('meta_keywords', models.TextField(blank=True, verbose_name='Keywords')),
                ('meta_description', models.TextField(blank=True, verbose_name='Description')),
                ('air_condition_repair_work', models.ManyToManyField(to='service.AirConditionRepairWork', blank=True, verbose_name='Кондиционер, радиаторы', related_name='air_condition_repair_work')),
                ('audio_alarm_repair_work', models.ManyToManyField(to='service.AudioAlarmRepairWork', blank=True, verbose_name='Аудио, Сигнализации', related_name='audio_alarm_repair_work')),
                ('auto_diag_work', models.ManyToManyField(to='service.AutoDiagWork', blank=True, verbose_name='Диагностика автомобилей', related_name='auto_diag_work')),
                ('autoglasses_repair_work', models.ManyToManyField(to='service.AutoglassesRepairWork', blank=True, verbose_name='Автостекла', related_name='autoglasses_repair_work')),
            ],
            options={
                'verbose_name': 'Автосервис',
                'verbose_name_plural': 'Автосервисы',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BodyRepairWork',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('work_name', models.CharField(max_length=200, verbose_name='Вид работы')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Кузовной ремонт',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BreakSystemRepairWork',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('work_name', models.CharField(max_length=200, verbose_name='Вид работы')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Тормозная система',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ElectricianWork',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('work_name', models.CharField(max_length=200, verbose_name='Вид работы')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Автоэлектрика',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EngineRepairWork',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('work_name', models.CharField(max_length=200, verbose_name='Вид работы')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Ремонт двигателя',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FuelSystemRepairWork',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('work_name', models.CharField(max_length=200, verbose_name='Вид работы')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Ремонт топливной системы',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GasAppliancesRepairWork',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('work_name', models.CharField(max_length=200, verbose_name='Вид работы')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Газовое оборудование',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='KppRepairWork',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('work_name', models.CharField(max_length=200, verbose_name='Вид работы')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Ремонт КПП',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OilReplaceWork',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('work_name', models.CharField(max_length=200, verbose_name='Вид работы')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Замена масла',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OtherAutogWork',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('work_name', models.CharField(max_length=200, verbose_name='Вид работы')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Прочее',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SuspensionRepairWork',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('work_name', models.CharField(max_length=200, verbose_name='Вид работы')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Ремонт подвески',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TuningWork',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('work_name', models.CharField(max_length=200, verbose_name='Вид работы')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Тюнинг',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='body_repair_work',
            field=models.ManyToManyField(to='service.BodyRepairWork', blank=True, verbose_name='Кузовной ремонт', related_name='body_repair_work'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='autoservice',
            name='break_system_repair_work',
            field=models.ManyToManyField(to='service.BreakSystemRepairWork', blank=True, verbose_name='Ремонт тормозной системы', related_name='break_system_repair_work'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='autoservice',
            name='electrician_work',
            field=models.ManyToManyField(to='service.ElectricianWork', blank=True, verbose_name='Автоэлектрика', related_name='electrician_work'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='autoservice',
            name='engine_repair_work',
            field=models.ManyToManyField(to='service.EngineRepairWork', blank=True, verbose_name='Ремонт двигателя', related_name='body_repair_work'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='autoservice',
            name='fuel_system_repair_work',
            field=models.ManyToManyField(to='service.FuelSystemRepairWork', blank=True, verbose_name='Ремонт топливной системы', related_name='fuel_system_repair_work'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='autoservice',
            name='gas_applianses_repair_work',
            field=models.ManyToManyField(to='service.GasAppliancesRepairWork', blank=True, verbose_name='Газовое оборудование', related_name='gas_applianses_repair_work'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='autoservice',
            name='kpp_repair_work',
            field=models.ManyToManyField(to='service.KppRepairWork', blank=True, verbose_name='Ремонт КПП', related_name='kpp_repair_work'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='autoservice',
            name='oil_replace_work',
            field=models.ManyToManyField(to='service.OilReplaceWork', blank=True, verbose_name='Замена масла', related_name='oil_replace_work'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='autoservice',
            name='other_auto_work',
            field=models.ManyToManyField(to='service.OtherAutogWork', blank=True, verbose_name='Прочее', related_name='other_auto_work'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='autoservice',
            name='suspension_repair_work',
            field=models.ManyToManyField(to='service.SuspensionRepairWork', blank=True, verbose_name='Ремонт подвески', related_name='suspension_repair_work'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='autoservice',
            name='tuning_work',
            field=models.ManyToManyField(to='service.TuningWork', blank=True, verbose_name='Тюнинг', related_name='tuning_work'),
            preserve_default=True,
        ),
    ]

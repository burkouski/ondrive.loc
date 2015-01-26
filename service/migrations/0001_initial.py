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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('work_name', models.CharField(verbose_name='Вид работы', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Кондиционер, радиаторы',
                'verbose_name': '',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AudioAlarmRepairWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('work_name', models.CharField(verbose_name='Вид работы', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Аудио, Сигнализации',
                'verbose_name': '',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AutoDiagWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('work_name', models.CharField(verbose_name='Вид работы', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Диагностика автомобилей',
                'verbose_name': '',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AutoglassesRepairWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('work_name', models.CharField(verbose_name='Вид работы', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Автостекла',
                'verbose_name': '',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AutoService',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Название сервиса', max_length=200)),
                ('alias', models.SlugField(blank=True, max_length=100)),
                ('teaser', models.TextField(verbose_name='Краткое описание')),
                ('address', models.CharField(verbose_name='Адрес', max_length=200)),
                ('phone_velcom', models.CharField(blank=True, verbose_name='Velcom', max_length=10)),
                ('phone_mts', models.CharField(blank=True, verbose_name='МТС', max_length=10)),
                ('phone_life', models.CharField(blank=True, verbose_name='Life', max_length=10)),
                ('phone_city', models.CharField(blank=True, verbose_name='Городской', max_length=10)),
                ('work_start', models.TimeField(verbose_name='Время начала работы', blank=True, null=True)),
                ('work_end', models.TimeField(verbose_name='Время завершения работы', blank=True, null=True)),
                ('break_time_start', models.TimeField(verbose_name='Время начала обеда', blank=True, null=True)),
                ('break_time_end', models.TimeField(verbose_name='Время завершения обеда', blank=True, null=True)),
                ('holiday', models.CharField(blank=True, verbose_name='Сокращенные дни', max_length=10)),
                ('holiday_time_start', models.TimeField(verbose_name='Время начала сокращенного дня', blank=True, null=True)),
                ('holiday_time_end', models.TimeField(verbose_name='Время завершения сокращенного дня', blank=True, null=True)),
                ('monday', models.BooleanField(verbose_name='Понедельник')),
                ('tuesday', models.BooleanField(verbose_name='Вторник')),
                ('wednesday', models.BooleanField(verbose_name='Среда')),
                ('thursday', models.BooleanField(verbose_name='Четверг')),
                ('friday', models.BooleanField(verbose_name='Пятница')),
                ('saturday', models.BooleanField(verbose_name='Суббота')),
                ('sunday', models.BooleanField(verbose_name='Воскресенье')),
                ('email', models.EmailField(blank=True, verbose_name='Email', max_length=75)),
                ('site_url', models.URLField(blank=True, verbose_name='Сайт')),
                ('full_desc', ckeditor.fields.RichTextField(verbose_name='Полное описание', blank=True)),
                ('logo', models.ImageField(blank=True, verbose_name='Логотип компании', upload_to='')),
                ('is_top', models.BooleanField(default=None, verbose_name='Выводить в топ на главной?')),
                ('latitude', models.CharField(blank=True, verbose_name='Широта', max_length=200)),
                ('longitude', models.CharField(blank=True, verbose_name='Долгота', max_length=200)),
                ('title', models.CharField(blank=True, verbose_name='title страницы', max_length=200)),
                ('meta_keywords', models.TextField(verbose_name='Keywords', blank=True)),
                ('meta_description', models.TextField(verbose_name='Description', blank=True)),
                ('air_condition_repair_work', models.ManyToManyField(to='service.AirConditionRepairWork', verbose_name='Кондиционер, радиаторы', related_name='air_condition_repair_work')),
                ('audio_alarm_repair_work', models.ManyToManyField(to='service.AudioAlarmRepairWork', verbose_name='Аудио, Сигнализации', related_name='audio_alarm_repair_work')),
                ('auto_diag_work', models.ManyToManyField(to='service.AutoDiagWork', verbose_name='Диагностика автомобилей', related_name='auto_diag_work')),
                ('autoglasses_repair_work', models.ManyToManyField(to='service.AutoglassesRepairWork', verbose_name='Автостекла', related_name='autoglasses_repair_work')),
            ],
            options={
                'verbose_name_plural': 'Автосервисы',
                'verbose_name': 'Автосервис',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BodyRepairWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('work_name', models.CharField(verbose_name='Вид работы', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Кузовной ремонт',
                'verbose_name': '',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BreakSystemRepairWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('work_name', models.CharField(verbose_name='Вид работы', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Тормозная система',
                'verbose_name': '',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ElectricianWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('work_name', models.CharField(verbose_name='Вид работы', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Автоэлектрика',
                'verbose_name': '',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EngineRepairWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('work_name', models.CharField(verbose_name='Вид работы', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Ремонт двигателя',
                'verbose_name': '',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FuelSystemRepairWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('work_name', models.CharField(verbose_name='Вид работы', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Ремонт топливной системы',
                'verbose_name': '',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GasAppliancesRepairWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('work_name', models.CharField(verbose_name='Вид работы', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Газовое оборудование',
                'verbose_name': '',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='KppRepairWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('work_name', models.CharField(verbose_name='Вид работы', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Ремонт КПП',
                'verbose_name': '',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OilReplaceWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('work_name', models.CharField(verbose_name='Вид работы', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Замена масла',
                'verbose_name': '',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OtherAutogWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('work_name', models.CharField(verbose_name='Вид работы', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Прочее',
                'verbose_name': '',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SuspensionRepairWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('work_name', models.CharField(verbose_name='Вид работы', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Ремонт подвески',
                'verbose_name': '',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TuningWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('work_name', models.CharField(verbose_name='Вид работы', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Тюнинг',
                'verbose_name': '',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='body_repair_work',
            field=models.ManyToManyField(to='service.BodyRepairWork', verbose_name='Кузовной ремонт', related_name='body_repair_work'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='autoservice',
            name='break_system_repair_work',
            field=models.ManyToManyField(to='service.BreakSystemRepairWork', verbose_name='Ремонт тормозной системы', related_name='break_system_repair_work'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='autoservice',
            name='electrician_work',
            field=models.ManyToManyField(to='service.ElectricianWork', verbose_name='Автоэлектрика', related_name='electrician_work'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='autoservice',
            name='engine_repair_work',
            field=models.ManyToManyField(to='service.EngineRepairWork', verbose_name='Ремонт двигателя', related_name='body_repair_work'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='autoservice',
            name='fuel_system_repair_work',
            field=models.ManyToManyField(to='service.FuelSystemRepairWork', verbose_name='Ремонт топливной системы', related_name='fuel_system_repair_work'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='autoservice',
            name='gas_applianses_repair_work',
            field=models.ManyToManyField(to='service.GasAppliancesRepairWork', verbose_name='Газовое оборудование', related_name='gas_applianses_repair_work'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='autoservice',
            name='kpp_repair_work',
            field=models.ManyToManyField(to='service.KppRepairWork', verbose_name='Ремонт КПП', related_name='kpp_repair_work'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='autoservice',
            name='oil_replace_work',
            field=models.ManyToManyField(to='service.OilReplaceWork', verbose_name='Замена масла', related_name='oil_replace_work'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='autoservice',
            name='other_auto_work',
            field=models.ManyToManyField(to='service.OtherAutogWork', verbose_name='Прочее', related_name='other_auto_work'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='autoservice',
            name='suspension_repair_work',
            field=models.ManyToManyField(to='service.SuspensionRepairWork', verbose_name='Ремонт подвески', related_name='suspension_repair_work'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='autoservice',
            name='tuning_work',
            field=models.ManyToManyField(to='service.TuningWork', verbose_name='Тюнинг', related_name='tuning_work'),
            preserve_default=True,
        ),
    ]

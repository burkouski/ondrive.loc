# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_auto_20150312_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addservices',
            name='work_name',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b'),
        ),
        migrations.AlterField(
            model_name='airconditionrepairwork',
            name='work_name',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b'),
        ),
        migrations.AlterField(
            model_name='audioalarmrepairwork',
            name='work_name',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b'),
        ),
        migrations.AlterField(
            model_name='autodiagwork',
            name='work_name',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b'),
        ),
        migrations.AlterField(
            model_name='autoglassesrepairwork',
            name='work_name',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b'),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='address',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x90\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81'),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='air_condition_repair_work',
            field=models.ManyToManyField(related_name='air_condition_repair_work', verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbd\xd0\xb4\xd0\xb8\xd1\x86\xd0\xb8\xd0\xbe\xd0\xbd\xd0\xb5\xd1\x80, \xd1\x80\xd0\xb0\xd0\xb4\xd0\xb8\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80\xd1\x8b', to='service.AirConditionRepairWork', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='audio_alarm_repair_work',
            field=models.ManyToManyField(related_name='audio_alarm_repair_work', verbose_name=b'\xd0\x90\xd1\x83\xd0\xb4\xd0\xb8\xd0\xbe, \xd0\xa1\xd0\xb8\xd0\xb3\xd0\xbd\xd0\xb0\xd0\xbb\xd0\xb8\xd0\xb7\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8', to='service.AudioAlarmRepairWork', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='auto_diag_work',
            field=models.ManyToManyField(related_name='auto_diag_work', verbose_name=b'\xd0\x94\xd0\xb8\xd0\xb0\xd0\xb3\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd0\xb8\xd0\xba\xd0\xb0 \xd0\xb0\xd0\xb2\xd1\x82\xd0\xbe\xd0\xbc\xd0\xbe\xd0\xb1\xd0\xb8\xd0\xbb\xd0\xb5\xd0\xb9', to='service.AutoDiagWork', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='autoglasses_repair_work',
            field=models.ManyToManyField(related_name='autoglasses_repair_work', verbose_name=b'\xd0\x90\xd0\xb2\xd1\x82\xd0\xbe\xd1\x81\xd1\x82\xd0\xb5\xd0\xba\xd0\xbb\xd0\xb0', to='service.AutoglassesRepairWork', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='body_repair_work',
            field=models.ManyToManyField(related_name='body_repair_work', verbose_name=b'\xd0\x9a\xd1\x83\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xbd\xd0\xbe\xd0\xb9 \xd1\x80\xd0\xb5\xd0\xbc\xd0\xbe\xd0\xbd\xd1\x82', to='service.BodyRepairWork', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='break_system_repair_work',
            field=models.ManyToManyField(related_name='break_system_repair_work', verbose_name=b'\xd0\xa0\xd0\xb5\xd0\xbc\xd0\xbe\xd0\xbd\xd1\x82 \xd1\x82\xd0\xbe\xd1\x80\xd0\xbc\xd0\xbe\xd0\xb7\xd0\xbd\xd0\xbe\xd0\xb9 \xd1\x81\xd0\xb8\xd1\x81\xd1\x82\xd0\xb5\xd0\xbc\xd1\x8b', to='service.BreakSystemRepairWork', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='break_time_end',
            field=models.TimeField(null=True, verbose_name=b'\xd0\x92\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xb7\xd0\xb0\xd0\xb2\xd0\xb5\xd1\x80\xd1\x88\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xbe\xd0\xb1\xd0\xb5\xd0\xb4\xd0\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='break_time_start',
            field=models.TimeField(null=True, verbose_name=b'\xd0\x92\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xbd\xd0\xb0\xd1\x87\xd0\xb0\xd0\xbb\xd0\xb0 \xd0\xbe\xd0\xb1\xd0\xb5\xd0\xb4\xd0\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='electrician_work',
            field=models.ManyToManyField(related_name='electrician_work', verbose_name=b'\xd0\x90\xd0\xb2\xd1\x82\xd0\xbe\xd1\x8d\xd0\xbb\xd0\xb5\xd0\xba\xd1\x82\xd1\x80\xd0\xb8\xd0\xba\xd0\xb0', to='service.ElectricianWork', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='email',
            field=models.EmailField(max_length=254, verbose_name=b'Email', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='engine_repair_work',
            field=models.ManyToManyField(related_name='body_repair_work', verbose_name=b'\xd0\xa0\xd0\xb5\xd0\xbc\xd0\xbe\xd0\xbd\xd1\x82 \xd0\xb4\xd0\xb2\xd0\xb8\xd0\xb3\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8f', to='service.EngineRepairWork', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='friday',
            field=models.BooleanField(default=None, verbose_name=b'\xd0\x9f\xd1\x8f\xd1\x82\xd0\xbd\xd0\xb8\xd1\x86\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='fuel_system_repair_work',
            field=models.ManyToManyField(related_name='fuel_system_repair_work', verbose_name=b'\xd0\xa0\xd0\xb5\xd0\xbc\xd0\xbe\xd0\xbd\xd1\x82 \xd1\x82\xd0\xbe\xd0\xbf\xd0\xbb\xd0\xb8\xd0\xb2\xd0\xbd\xd0\xbe\xd0\xb9 \xd1\x81\xd0\xb8\xd1\x81\xd1\x82\xd0\xb5\xd0\xbc\xd1\x8b', to='service.FuelSystemRepairWork', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='full_desc',
            field=ckeditor.fields.RichTextField(verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xbe\xd0\xb5 \xd0\xbe\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='gas_applianses_repair_work',
            field=models.ManyToManyField(related_name='gas_applianses_repair_work', verbose_name=b'\xd0\x93\xd0\xb0\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xb5 \xd0\xbe\xd0\xb1\xd0\xbe\xd1\x80\xd1\x83\xd0\xb4\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', to='service.GasAppliancesRepairWork', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='holiday',
            field=models.CharField(max_length=10, verbose_name=b'\xd0\xa1\xd0\xbe\xd0\xba\xd1\x80\xd0\xb0\xd1\x89\xd0\xb5\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xb5 \xd0\xb4\xd0\xbd\xd0\xb8', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='holiday_time_end',
            field=models.TimeField(null=True, verbose_name=b'\xd0\x92\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xb7\xd0\xb0\xd0\xb2\xd0\xb5\xd1\x80\xd1\x88\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd1\x81\xd0\xbe\xd0\xba\xd1\x80\xd0\xb0\xd1\x89\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xbe\xd0\xb3\xd0\xbe \xd0\xb4\xd0\xbd\xd1\x8f', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='holiday_time_start',
            field=models.TimeField(null=True, verbose_name=b'\xd0\x92\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xbd\xd0\xb0\xd1\x87\xd0\xb0\xd0\xbb\xd0\xb0 \xd1\x81\xd0\xbe\xd0\xba\xd1\x80\xd0\xb0\xd1\x89\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xbe\xd0\xb3\xd0\xbe \xd0\xb4\xd0\xbd\xd1\x8f', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='is_top',
            field=models.BooleanField(default=None, verbose_name=b'\xd0\x92\xd1\x8b\xd0\xb2\xd0\xbe\xd0\xb4\xd0\xb8\xd1\x82\xd1\x8c \xd0\xb2 \xd1\x82\xd0\xbe\xd0\xbf \xd0\xbd\xd0\xb0 \xd0\xb3\xd0\xbb\xd0\xb0\xd0\xb2\xd0\xbd\xd0\xbe\xd0\xb9?'),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='kpp_repair_work',
            field=models.ManyToManyField(related_name='kpp_repair_work', verbose_name=b'\xd0\xa0\xd0\xb5\xd0\xbc\xd0\xbe\xd0\xbd\xd1\x82 \xd0\x9a\xd0\x9f\xd0\x9f', to='service.KppRepairWork', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='latitude',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\xa8\xd0\xb8\xd1\x80\xd0\xbe\xd1\x82\xd0\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='logo',
            field=models.ImageField(upload_to=b'', verbose_name=b'\xd0\x9b\xd0\xbe\xd0\xb3\xd0\xbe\xd1\x82\xd0\xb8\xd0\xbf \xd0\xba\xd0\xbe\xd0\xbc\xd0\xbf\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb8', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='longitude',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x94\xd0\xbe\xd0\xbb\xd0\xb3\xd0\xbe\xd1\x82\xd0\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='monday',
            field=models.BooleanField(default=None, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbd\xd0\xb5\xd0\xb4\xd0\xb5\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xb8\xd0\xba'),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='name',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x81\xd0\xb5\xd1\x80\xd0\xb2\xd0\xb8\xd1\x81\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='oil_replace_work',
            field=models.ManyToManyField(related_name='oil_replace_work', verbose_name=b'\xd0\x97\xd0\xb0\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb0 \xd0\xbc\xd0\xb0\xd1\x81\xd0\xbb\xd0\xb0', to='service.OilReplaceWork', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='other_auto_work',
            field=models.ManyToManyField(related_name='other_auto_work', verbose_name=b'\xd0\x9f\xd1\x80\xd0\xbe\xd1\x87\xd0\xb5\xd0\xb5', to='service.OtherAutogWork', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='phone_city',
            field=models.CharField(max_length=20, verbose_name=b'\xd0\x93\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4\xd1\x81\xd0\xba\xd0\xbe\xd0\xb9', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='phone_city2',
            field=models.CharField(max_length=20, verbose_name=b'\xd0\xb2\xd1\x82\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb9 \xd0\x93\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4\xd1\x81\xd0\xba\xd0\xbe\xd0\xb9', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='phone_life2',
            field=models.CharField(max_length=20, verbose_name=b'\xd0\xb2\xd1\x82\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb9 Life', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='phone_mts',
            field=models.CharField(max_length=20, verbose_name=b'\xd0\x9c\xd0\xa2\xd0\xa1', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='phone_mts2',
            field=models.CharField(max_length=10, verbose_name=b'\xd0\xb2\xd1\x82\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb9 \xd0\x9c\xd0\xa2\xd0\xa1', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='phone_velcom2',
            field=models.CharField(max_length=20, verbose_name=b'\xd0\xb2\xd1\x82\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb9 Velcom', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='saturday',
            field=models.BooleanField(default=None, verbose_name=b'\xd0\xa1\xd1\x83\xd0\xb1\xd0\xb1\xd0\xbe\xd1\x82\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='site_url',
            field=models.URLField(verbose_name=b'\xd0\xa1\xd0\xb0\xd0\xb9\xd1\x82', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='sunday',
            field=models.BooleanField(default=None, verbose_name=b'\xd0\x92\xd0\xbe\xd1\x81\xd0\xba\xd1\x80\xd0\xb5\xd1\x81\xd0\xb5\xd0\xbd\xd1\x8c\xd0\xb5'),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='suspension_repair_work',
            field=models.ManyToManyField(related_name='suspension_repair_work', verbose_name=b'\xd0\xa0\xd0\xb5\xd0\xbc\xd0\xbe\xd0\xbd\xd1\x82 \xd0\xbf\xd0\xbe\xd0\xb4\xd0\xb2\xd0\xb5\xd1\x81\xd0\xba\xd0\xb8', to='service.SuspensionRepairWork', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='teaser',
            field=models.TextField(verbose_name=b'\xd0\x9a\xd1\x80\xd0\xb0\xd1\x82\xd0\xba\xd0\xbe\xd0\xb5 \xd0\xbe\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='thursday',
            field=models.BooleanField(default=None, verbose_name=b'\xd0\xa7\xd0\xb5\xd1\x82\xd0\xb2\xd0\xb5\xd1\x80\xd0\xb3'),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='title',
            field=models.CharField(max_length=200, verbose_name=b'title \xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x86\xd1\x8b', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='tuesday',
            field=models.BooleanField(default=None, verbose_name=b'\xd0\x92\xd1\x82\xd0\xbe\xd1\x80\xd0\xbd\xd0\xb8\xd0\xba'),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='tuning_work',
            field=models.ManyToManyField(related_name='tuning_work', verbose_name=b'\xd0\xa2\xd1\x8e\xd0\xbd\xd0\xb8\xd0\xbd\xd0\xb3', to='service.TuningWork', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='wednesday',
            field=models.BooleanField(default=None, verbose_name=b'\xd0\xa1\xd1\x80\xd0\xb5\xd0\xb4\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='work_end',
            field=models.TimeField(null=True, verbose_name=b'\xd0\x92\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xb7\xd0\xb0\xd0\xb2\xd0\xb5\xd1\x80\xd1\x88\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='work_start',
            field=models.TimeField(null=True, verbose_name=b'\xd0\x92\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xbd\xd0\xb0\xd1\x87\xd0\xb0\xd0\xbb\xd0\xb0 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b', blank=True),
        ),
        migrations.AlterField(
            model_name='bodyrepairwork',
            name='work_name',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b'),
        ),
        migrations.AlterField(
            model_name='breaksystemrepairwork',
            name='work_name',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b'),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='add_services',
            field=models.ManyToManyField(related_name='add_services', verbose_name=b'\xd0\x94\xd0\xbe\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x8b\xd0\xb5 \xd1\x83\xd1\x81\xd0\xbb\xd1\x83\xd0\xb3\xd0\xb8', to='service.AddServices', blank=True),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='address',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x90\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81'),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='break_time_end',
            field=models.TimeField(null=True, verbose_name=b'\xd0\x92\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xb7\xd0\xb0\xd0\xb2\xd0\xb5\xd1\x80\xd1\x88\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xbe\xd0\xb1\xd0\xb5\xd0\xb4\xd0\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='break_time_start',
            field=models.TimeField(null=True, verbose_name=b'\xd0\x92\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xbd\xd0\xb0\xd1\x87\xd0\xb0\xd0\xbb\xd0\xb0 \xd0\xbe\xd0\xb1\xd0\xb5\xd0\xb4\xd0\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='car_wash_services',
            field=models.ManyToManyField(related_name='car_wash_services', verbose_name=b'\xd0\xa3\xd1\x81\xd0\xbb\xd1\x83\xd0\xb3\xd0\xb8', to='service.CarWashServices', blank=True),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='email',
            field=models.EmailField(max_length=254, verbose_name=b'Email', blank=True),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='friday',
            field=models.BooleanField(default=None, verbose_name=b'\xd0\x9f\xd1\x8f\xd1\x82\xd0\xbd\xd0\xb8\xd1\x86\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='full_desc',
            field=ckeditor.fields.RichTextField(verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xbe\xd0\xb5 \xd0\xbe\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='holiday',
            field=models.CharField(max_length=10, verbose_name=b'\xd0\xa1\xd0\xbe\xd0\xba\xd1\x80\xd0\xb0\xd1\x89\xd0\xb5\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xb5 \xd0\xb4\xd0\xbd\xd0\xb8', blank=True),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='holiday_time_end',
            field=models.TimeField(null=True, verbose_name=b'\xd0\x92\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xb7\xd0\xb0\xd0\xb2\xd0\xb5\xd1\x80\xd1\x88\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd1\x81\xd0\xbe\xd0\xba\xd1\x80\xd0\xb0\xd1\x89\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xbe\xd0\xb3\xd0\xbe \xd0\xb4\xd0\xbd\xd1\x8f', blank=True),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='holiday_time_start',
            field=models.TimeField(null=True, verbose_name=b'\xd0\x92\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xbd\xd0\xb0\xd1\x87\xd0\xb0\xd0\xbb\xd0\xb0 \xd1\x81\xd0\xbe\xd0\xba\xd1\x80\xd0\xb0\xd1\x89\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xbe\xd0\xb3\xd0\xbe \xd0\xb4\xd0\xbd\xd1\x8f', blank=True),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='is_top',
            field=models.BooleanField(default=None, verbose_name=b'\xd0\x92\xd1\x8b\xd0\xb2\xd0\xbe\xd0\xb4\xd0\xb8\xd1\x82\xd1\x8c \xd0\xb2 \xd1\x82\xd0\xbe\xd0\xbf \xd0\xbd\xd0\xb0 \xd0\xb3\xd0\xbb\xd0\xb0\xd0\xb2\xd0\xbd\xd0\xbe\xd0\xb9?'),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='latitude',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\xa8\xd0\xb8\xd1\x80\xd0\xbe\xd1\x82\xd0\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='logo',
            field=models.ImageField(upload_to=b'', verbose_name=b'\xd0\x9b\xd0\xbe\xd0\xb3\xd0\xbe\xd1\x82\xd0\xb8\xd0\xbf \xd0\xba\xd0\xbe\xd0\xbc\xd0\xbf\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb8', blank=True),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='longitude',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x94\xd0\xbe\xd0\xbb\xd0\xb3\xd0\xbe\xd1\x82\xd0\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='monday',
            field=models.BooleanField(default=None, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbd\xd0\xb5\xd0\xb4\xd0\xb5\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xb8\xd0\xba'),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='name',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x81\xd0\xb5\xd1\x80\xd0\xb2\xd0\xb8\xd1\x81\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='phone_city',
            field=models.CharField(max_length=20, verbose_name=b'\xd0\x93\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4\xd1\x81\xd0\xba\xd0\xbe\xd0\xb9', blank=True),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='phone_city2',
            field=models.CharField(max_length=20, verbose_name=b'\xd0\xb2\xd1\x82\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb9 \xd0\x93\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4\xd1\x81\xd0\xba\xd0\xbe\xd0\xb9', blank=True),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='phone_life2',
            field=models.CharField(max_length=20, verbose_name=b'\xd0\xb2\xd1\x82\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb9 Life', blank=True),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='phone_mts',
            field=models.CharField(max_length=20, verbose_name=b'\xd0\x9c\xd0\xa2\xd0\xa1', blank=True),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='phone_mts2',
            field=models.CharField(max_length=10, verbose_name=b'\xd0\xb2\xd1\x82\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb9 \xd0\x9c\xd0\xa2\xd0\xa1', blank=True),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='phone_velcom2',
            field=models.CharField(max_length=20, verbose_name=b'\xd0\xb2\xd1\x82\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb9 Velcom', blank=True),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='saturday',
            field=models.BooleanField(default=None, verbose_name=b'\xd0\xa1\xd1\x83\xd0\xb1\xd0\xb1\xd0\xbe\xd1\x82\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='site_url',
            field=models.URLField(verbose_name=b'\xd0\xa1\xd0\xb0\xd0\xb9\xd1\x82', blank=True),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='sunday',
            field=models.BooleanField(default=None, verbose_name=b'\xd0\x92\xd0\xbe\xd1\x81\xd0\xba\xd1\x80\xd0\xb5\xd1\x81\xd0\xb5\xd0\xbd\xd1\x8c\xd0\xb5'),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='teaser',
            field=models.TextField(verbose_name=b'\xd0\x9a\xd1\x80\xd0\xb0\xd1\x82\xd0\xba\xd0\xbe\xd0\xb5 \xd0\xbe\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='thursday',
            field=models.BooleanField(default=None, verbose_name=b'\xd0\xa7\xd0\xb5\xd1\x82\xd0\xb2\xd0\xb5\xd1\x80\xd0\xb3'),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='title',
            field=models.CharField(max_length=200, verbose_name=b'title \xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x86\xd1\x8b', blank=True),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='tuesday',
            field=models.BooleanField(default=None, verbose_name=b'\xd0\x92\xd1\x82\xd0\xbe\xd1\x80\xd0\xbd\xd0\xb8\xd0\xba'),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='type_carwash',
            field=models.ManyToManyField(related_name='type_carwash', verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd0\xbc\xd0\xbe\xd0\xb9\xd0\xba\xd0\xb8', to='service.TypeCarWash', blank=True),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='type_vehicle',
            field=models.ManyToManyField(related_name='type_vehicle', verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd1\x82\xd1\x80\xd0\xb0\xd0\xbd\xd1\x81\xd0\xbf\xd0\xbe\xd1\x80\xd1\x82\xd0\xb0', to='service.TypeVehicle', blank=True),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='wednesday',
            field=models.BooleanField(default=None, verbose_name=b'\xd0\xa1\xd1\x80\xd0\xb5\xd0\xb4\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='work_end',
            field=models.TimeField(null=True, verbose_name=b'\xd0\x92\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xb7\xd0\xb0\xd0\xb2\xd0\xb5\xd1\x80\xd1\x88\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b', blank=True),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='work_start',
            field=models.TimeField(null=True, verbose_name=b'\xd0\x92\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xbd\xd0\xb0\xd1\x87\xd0\xb0\xd0\xbb\xd0\xb0 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b', blank=True),
        ),
        migrations.AlterField(
            model_name='carwashservices',
            name='work_name',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b'),
        ),
        migrations.AlterField(
            model_name='discwork',
            name='work_name',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b'),
        ),
        migrations.AlterField(
            model_name='electricianwork',
            name='work_name',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b'),
        ),
        migrations.AlterField(
            model_name='enginerepairwork',
            name='work_name',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b'),
        ),
        migrations.AlterField(
            model_name='fuelsystemrepairwork',
            name='work_name',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b'),
        ),
        migrations.AlterField(
            model_name='gasappliancesrepairwork',
            name='work_name',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b'),
        ),
        migrations.AlterField(
            model_name='kpprepairwork',
            name='work_name',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b'),
        ),
        migrations.AlterField(
            model_name='oilreplacework',
            name='work_name',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b'),
        ),
        migrations.AlterField(
            model_name='otherautogwork',
            name='work_name',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b'),
        ),
        migrations.AlterField(
            model_name='suspensionrepairwork',
            name='work_name',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b'),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='add_services',
            field=models.ManyToManyField(related_name='tire_add_services', verbose_name=b'\xd0\x94\xd0\xbe\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x8b\xd0\xb5 \xd1\x83\xd1\x81\xd0\xbb\xd1\x83\xd0\xb3\xd0\xb8', to='service.AddServices', blank=True),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='address',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x90\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81'),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='break_time_end',
            field=models.TimeField(null=True, verbose_name=b'\xd0\x92\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xb7\xd0\xb0\xd0\xb2\xd0\xb5\xd1\x80\xd1\x88\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xbe\xd0\xb1\xd0\xb5\xd0\xb4\xd0\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='break_time_start',
            field=models.TimeField(null=True, verbose_name=b'\xd0\x92\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xbd\xd0\xb0\xd1\x87\xd0\xb0\xd0\xbb\xd0\xb0 \xd0\xbe\xd0\xb1\xd0\xb5\xd0\xb4\xd0\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='disc_work',
            field=models.ManyToManyField(related_name='disc_work', verbose_name=b'\xd0\x94\xd0\xb8\xd1\x81\xd0\xba\xd0\xb8', to='service.DiscWork', blank=True),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='email',
            field=models.EmailField(max_length=254, verbose_name=b'Email', blank=True),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='friday',
            field=models.BooleanField(default=None, verbose_name=b'\xd0\x9f\xd1\x8f\xd1\x82\xd0\xbd\xd0\xb8\xd1\x86\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='full_desc',
            field=ckeditor.fields.RichTextField(verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xbe\xd0\xb5 \xd0\xbe\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='holiday',
            field=models.CharField(max_length=10, verbose_name=b'\xd0\xa1\xd0\xbe\xd0\xba\xd1\x80\xd0\xb0\xd1\x89\xd0\xb5\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xb5 \xd0\xb4\xd0\xbd\xd0\xb8', blank=True),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='holiday_time_end',
            field=models.TimeField(null=True, verbose_name=b'\xd0\x92\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xb7\xd0\xb0\xd0\xb2\xd0\xb5\xd1\x80\xd1\x88\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd1\x81\xd0\xbe\xd0\xba\xd1\x80\xd0\xb0\xd1\x89\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xbe\xd0\xb3\xd0\xbe \xd0\xb4\xd0\xbd\xd1\x8f', blank=True),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='holiday_time_start',
            field=models.TimeField(null=True, verbose_name=b'\xd0\x92\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xbd\xd0\xb0\xd1\x87\xd0\xb0\xd0\xbb\xd0\xb0 \xd1\x81\xd0\xbe\xd0\xba\xd1\x80\xd0\xb0\xd1\x89\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xbe\xd0\xb3\xd0\xbe \xd0\xb4\xd0\xbd\xd1\x8f', blank=True),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='is_top',
            field=models.BooleanField(default=None, verbose_name=b'\xd0\x92\xd1\x8b\xd0\xb2\xd0\xbe\xd0\xb4\xd0\xb8\xd1\x82\xd1\x8c \xd0\xb2 \xd1\x82\xd0\xbe\xd0\xbf \xd0\xbd\xd0\xb0 \xd0\xb3\xd0\xbb\xd0\xb0\xd0\xb2\xd0\xbd\xd0\xbe\xd0\xb9?'),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='latitude',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\xa8\xd0\xb8\xd1\x80\xd0\xbe\xd1\x82\xd0\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='logo',
            field=models.ImageField(upload_to=b'', verbose_name=b'\xd0\x9b\xd0\xbe\xd0\xb3\xd0\xbe\xd1\x82\xd0\xb8\xd0\xbf \xd0\xba\xd0\xbe\xd0\xbc\xd0\xbf\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb8', blank=True),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='longitude',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x94\xd0\xbe\xd0\xbb\xd0\xb3\xd0\xbe\xd1\x82\xd0\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='monday',
            field=models.BooleanField(default=None, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbd\xd0\xb5\xd0\xb4\xd0\xb5\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xb8\xd0\xba'),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='name',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x81\xd0\xb5\xd1\x80\xd0\xb2\xd0\xb8\xd1\x81\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='phone_city',
            field=models.CharField(max_length=20, verbose_name=b'\xd0\x93\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4\xd1\x81\xd0\xba\xd0\xbe\xd0\xb9', blank=True),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='phone_city2',
            field=models.CharField(max_length=20, verbose_name=b'\xd0\xb2\xd1\x82\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb9 \xd0\x93\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4\xd1\x81\xd0\xba\xd0\xbe\xd0\xb9', blank=True),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='phone_life2',
            field=models.CharField(max_length=20, verbose_name=b'\xd0\xb2\xd1\x82\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb9 Life', blank=True),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='phone_mts',
            field=models.CharField(max_length=20, verbose_name=b'\xd0\x9c\xd0\xa2\xd0\xa1', blank=True),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='phone_mts2',
            field=models.CharField(max_length=10, verbose_name=b'\xd0\xb2\xd1\x82\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb9 \xd0\x9c\xd0\xa2\xd0\xa1', blank=True),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='phone_velcom2',
            field=models.CharField(max_length=20, verbose_name=b'\xd0\xb2\xd1\x82\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb9 Velcom', blank=True),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='saturday',
            field=models.BooleanField(default=None, verbose_name=b'\xd0\xa1\xd1\x83\xd0\xb1\xd0\xb1\xd0\xbe\xd1\x82\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='site_url',
            field=models.URLField(verbose_name=b'\xd0\xa1\xd0\xb0\xd0\xb9\xd1\x82', blank=True),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='sunday',
            field=models.BooleanField(default=None, verbose_name=b'\xd0\x92\xd0\xbe\xd1\x81\xd0\xba\xd1\x80\xd0\xb5\xd1\x81\xd0\xb5\xd0\xbd\xd1\x8c\xd0\xb5'),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='teaser',
            field=models.TextField(verbose_name=b'\xd0\x9a\xd1\x80\xd0\xb0\xd1\x82\xd0\xba\xd0\xbe\xd0\xb5 \xd0\xbe\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='thursday',
            field=models.BooleanField(default=None, verbose_name=b'\xd0\xa7\xd0\xb5\xd1\x82\xd0\xb2\xd0\xb5\xd1\x80\xd0\xb3'),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='tire_work',
            field=models.ManyToManyField(related_name='tire_work', verbose_name=b'\xd0\xa8\xd0\xb8\xd0\xbd\xd1\x8b', to='service.TireWork', blank=True),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='title',
            field=models.CharField(max_length=200, verbose_name=b'title \xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x86\xd1\x8b', blank=True),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='tuesday',
            field=models.BooleanField(default=None, verbose_name=b'\xd0\x92\xd1\x82\xd0\xbe\xd1\x80\xd0\xbd\xd0\xb8\xd0\xba'),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='wednesday',
            field=models.BooleanField(default=None, verbose_name=b'\xd0\xa1\xd1\x80\xd0\xb5\xd0\xb4\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='work_end',
            field=models.TimeField(null=True, verbose_name=b'\xd0\x92\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xb7\xd0\xb0\xd0\xb2\xd0\xb5\xd1\x80\xd1\x88\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b', blank=True),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='work_start',
            field=models.TimeField(null=True, verbose_name=b'\xd0\x92\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xbd\xd0\xb0\xd1\x87\xd0\xb0\xd0\xbb\xd0\xb0 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b', blank=True),
        ),
        migrations.AlterField(
            model_name='tirework',
            name='work_name',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b'),
        ),
        migrations.AlterField(
            model_name='tuningwork',
            name='work_name',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b'),
        ),
        migrations.AlterField(
            model_name='typecarwash',
            name='work_name',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b'),
        ),
        migrations.AlterField(
            model_name='typevehicle',
            name='work_name',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b'),
        ),
    ]

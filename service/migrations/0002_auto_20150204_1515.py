# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='autoservice',
            name='phone_city2',
            field=models.CharField(max_length=10, verbose_name='Городской', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='autoservice',
            name='phone_life2',
            field=models.CharField(max_length=10, verbose_name='Life', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='autoservice',
            name='phone_mts2',
            field=models.CharField(max_length=10, verbose_name='МТС', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='autoservice',
            name='phone_velcom2',
            field=models.CharField(max_length=10, verbose_name='Velcom', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='air_condition_repair_work',
            field=models.ManyToManyField(verbose_name='Кондиционер, радиаторы', related_name='air_condition_repair_work', blank=True, to='service.AirConditionRepairWork'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='audio_alarm_repair_work',
            field=models.ManyToManyField(verbose_name='Аудио, Сигнализации', related_name='audio_alarm_repair_work', blank=True, to='service.AudioAlarmRepairWork'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='auto_diag_work',
            field=models.ManyToManyField(verbose_name='Диагностика автомобилей', related_name='auto_diag_work', blank=True, to='service.AutoDiagWork'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='autoglasses_repair_work',
            field=models.ManyToManyField(verbose_name='Автостекла', related_name='autoglasses_repair_work', blank=True, to='service.AutoglassesRepairWork'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='body_repair_work',
            field=models.ManyToManyField(verbose_name='Кузовной ремонт', related_name='body_repair_work', blank=True, to='service.BodyRepairWork'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='break_system_repair_work',
            field=models.ManyToManyField(verbose_name='Ремонт тормозной системы', related_name='break_system_repair_work', blank=True, to='service.BreakSystemRepairWork'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='electrician_work',
            field=models.ManyToManyField(verbose_name='Автоэлектрика', related_name='electrician_work', blank=True, to='service.ElectricianWork'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='engine_repair_work',
            field=models.ManyToManyField(verbose_name='Ремонт двигателя', related_name='body_repair_work', blank=True, to='service.EngineRepairWork'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='fuel_system_repair_work',
            field=models.ManyToManyField(verbose_name='Ремонт топливной системы', related_name='fuel_system_repair_work', blank=True, to='service.FuelSystemRepairWork'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='gas_applianses_repair_work',
            field=models.ManyToManyField(verbose_name='Газовое оборудование', related_name='gas_applianses_repair_work', blank=True, to='service.GasAppliancesRepairWork'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='kpp_repair_work',
            field=models.ManyToManyField(verbose_name='Ремонт КПП', related_name='kpp_repair_work', blank=True, to='service.KppRepairWork'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='oil_replace_work',
            field=models.ManyToManyField(verbose_name='Замена масла', related_name='oil_replace_work', blank=True, to='service.OilReplaceWork'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='other_auto_work',
            field=models.ManyToManyField(verbose_name='Прочее', related_name='other_auto_work', blank=True, to='service.OtherAutogWork'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='suspension_repair_work',
            field=models.ManyToManyField(verbose_name='Ремонт подвески', related_name='suspension_repair_work', blank=True, to='service.SuspensionRepairWork'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='tuning_work',
            field=models.ManyToManyField(verbose_name='Тюнинг', related_name='tuning_work', blank=True, to='service.TuningWork'),
            preserve_default=True,
        ),
    ]

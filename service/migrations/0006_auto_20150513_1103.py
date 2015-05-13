# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_auto_20150510_1653'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FuelSystemRepairWork',
            new_name='AutoserviceWork',
        ),
        migrations.RenameModel(
            old_name='TuningWork',
            new_name='SpecializationWork',
        ),
        migrations.AlterModelOptions(
            name='autoservicework',
            options={'verbose_name': '', 'verbose_name_plural': '\u0412\u0438\u0434\u044b \u0440\u0430\u0431\u043e\u0442'},
        ),
        migrations.AlterModelOptions(
            name='specializationwork',
            options={'verbose_name': '', 'verbose_name_plural': '\u0410\u0432\u0442\u043e\u044d\u043b\u0435\u043a\u0442\u0440\u0438\u043a\u0430'},
        ),
        migrations.RemoveField(
            model_name='autoservice',
            name='air_condition_repair_work',
        ),
        migrations.RemoveField(
            model_name='autoservice',
            name='audio_alarm_repair_work',
        ),
        migrations.RemoveField(
            model_name='autoservice',
            name='auto_diag_work',
        ),
        migrations.RemoveField(
            model_name='autoservice',
            name='autoglasses_repair_work',
        ),
        migrations.RemoveField(
            model_name='autoservice',
            name='body_repair_work',
        ),
        migrations.RemoveField(
            model_name='autoservice',
            name='break_system_repair_work',
        ),
        migrations.RemoveField(
            model_name='autoservice',
            name='electrician_work',
        ),
        migrations.RemoveField(
            model_name='autoservice',
            name='engine_repair_work',
        ),
        migrations.RemoveField(
            model_name='autoservice',
            name='fuel_system_repair_work',
        ),
        migrations.RemoveField(
            model_name='autoservice',
            name='gas_applianses_repair_work',
        ),
        migrations.RemoveField(
            model_name='autoservice',
            name='kpp_repair_work',
        ),
        migrations.RemoveField(
            model_name='autoservice',
            name='oil_replace_work',
        ),
        migrations.RemoveField(
            model_name='autoservice',
            name='other_auto_work',
        ),
        migrations.RemoveField(
            model_name='autoservice',
            name='suspension_repair_work',
        ),
        migrations.RemoveField(
            model_name='autoservice',
            name='tuning_work',
        ),
        migrations.AddField(
            model_name='autoservice',
            name='add_services',
            field=models.ManyToManyField(related_name='autoservice_add_services', verbose_name=b'\xd0\x94\xd0\xbe\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x8b\xd0\xb5 \xd1\x83\xd1\x81\xd0\xbb\xd1\x83\xd0\xb3\xd0\xb8', to='service.AddServices', blank=True),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='autoservice_work',
            field=models.ManyToManyField(related_name='autoservice_work', verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4\xd1\x8b \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82', to='service.AutoserviceWork', blank=True),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='specialization_work',
            field=models.ManyToManyField(related_name='specialization_work', verbose_name=b'\xd0\xa1\xd0\xbf\xd0\xb5\xd1\x86\xd0\xb8\xd0\xb0\xd0\xbb\xd0\xb8\xd0\xb7\xd0\xb8\xd1\x80\xd1\x83\xd1\x8e\xd1\x89\xd0\xb8\xd0\xb5\xd1\x81\xd1\x8f \xd0\xbd\xd0\xb0 \xd0\xbc\xd0\xb0\xd1\x80\xd0\xba\xd0\xb5', to='service.SpecializationWork', blank=True),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='add_services',
            field=models.ManyToManyField(related_name='carwash_add_services', verbose_name=b'\xd0\x94\xd0\xbe\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x8b\xd0\xb5 \xd1\x83\xd1\x81\xd0\xbb\xd1\x83\xd0\xb3\xd0\xb8', to='service.AddServices', blank=True),
        ),
        migrations.DeleteModel(
            name='AirConditionRepairWork',
        ),
        migrations.DeleteModel(
            name='AudioAlarmRepairWork',
        ),
        migrations.DeleteModel(
            name='AutoDiagWork',
        ),
        migrations.DeleteModel(
            name='AutoglassesRepairWork',
        ),
        migrations.DeleteModel(
            name='BodyRepairWork',
        ),
        migrations.DeleteModel(
            name='BreakSystemRepairWork',
        ),
        migrations.DeleteModel(
            name='ElectricianWork',
        ),
        migrations.DeleteModel(
            name='EngineRepairWork',
        ),
        migrations.DeleteModel(
            name='GasAppliancesRepairWork',
        ),
        migrations.DeleteModel(
            name='KppRepairWork',
        ),
        migrations.DeleteModel(
            name='OilReplaceWork',
        ),
        migrations.DeleteModel(
            name='OtherAutogWork',
        ),
        migrations.DeleteModel(
            name='SuspensionRepairWork',
        ),
    ]

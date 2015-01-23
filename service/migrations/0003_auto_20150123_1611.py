# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20150123_1039'),
    ]

    operations = [
        migrations.CreateModel(
            name='EngineRepairWork',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('work_name', models.CharField(verbose_name='Вид работы', max_length=200)),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Ремонт двигателя',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='engine_repair_work',
            field=models.ManyToManyField(related_name='body_repair_work', to='service.EngineRepairWork'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='electrician_work',
            field=models.ManyToManyField(related_name='electrician_work', to='service.ElectricianWork', verbose_name='Автоэлектрика'),
            preserve_default=True,
        ),
    ]

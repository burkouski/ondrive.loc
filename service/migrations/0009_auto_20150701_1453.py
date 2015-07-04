# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0008_auto_20150521_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='addservices',
            name='logo',
            field=models.ImageField(upload_to=b'', verbose_name=b'\xd0\xb8\xd0\xba\xd0\xbe\xd0\xbd\xd0\xba\xd0\xb0 \xd1\x83\xd1\x81\xd0\xbb\xd1\x83\xd0\xb3\xd0\xb8', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='add_services',
            field=models.ManyToManyField(related_name='autoservice_add_services', verbose_name='\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u0443\u0441\u043b\u0443\u0433\u0438', to='service.AddServices', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='add_work',
            field=models.ManyToManyField(related_name='add_work', verbose_name='\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u0440\u0430\u0431\u043e\u0442\u044b', to='service.AddWork', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='diag_work',
            field=models.ManyToManyField(related_name='diag_work', verbose_name='\u0414\u0438\u0430\u0433\u043d\u043e\u0441\u0442\u0438\u043a\u0430', to='service.DiagWork', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='repair_work',
            field=models.ManyToManyField(related_name='repair_work', verbose_name='\u0420\u0435\u043c\u043e\u043d\u0442', to='service.RepairWork', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='serv_work',
            field=models.ManyToManyField(related_name='serv_work', verbose_name='\u041e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u043d\u0438\u0435', to='service.ServWork', blank=True),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='specialization_work',
            field=models.ManyToManyField(related_name='specialization_work', verbose_name='\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0437\u0438\u0440\u0443\u044e\u0449\u0438\u0435\u0441\u044f \u043d\u0430 \u043c\u0430\u0440\u043a\u0435', to='service.SpecializationWork', blank=True),
        ),
    ]

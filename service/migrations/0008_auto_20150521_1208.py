# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_auto_20150513_1451'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiagWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('work_name', models.CharField(max_length=200, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '\u0414\u0438\u0430\u0433\u043d\u043e\u0441\u0442\u0438\u043a\u0430',
            },
        ),
        migrations.CreateModel(
            name='RepairWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('work_name', models.CharField(max_length=200, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '\u0420\u0435\u043c\u043e\u043d\u0442',
            },
        ),
        migrations.CreateModel(
            name='ServWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('work_name', models.CharField(max_length=200, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '\u041e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u043d\u0438\u0435',
            },
        ),
        migrations.RenameModel(
            old_name='AutoserviceWork',
            new_name='AddWork',
        ),
        migrations.AlterModelOptions(
            name='addwork',
            options={'verbose_name': '', 'verbose_name_plural': '\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u0440\u0430\u0431\u043e\u0442\u044b'},
        ),
        migrations.RemoveField(
            model_name='autoservice',
            name='autoservice_work',
        ),
        migrations.AddField(
            model_name='autoservice',
            name='add_work',
            field=models.ManyToManyField(related_name='add_work', verbose_name=b'\xd0\x94\xd0\xbe\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x8b\xd0\xb5 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b', to='service.AddWork', blank=True),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='diag_work',
            field=models.ManyToManyField(related_name='diag_work', verbose_name=b'\xd0\x94\xd0\xb8\xd0\xb0\xd0\xb3\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd0\xb8\xd0\xba\xd0\xb0', to='service.DiagWork', blank=True),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='repair_work',
            field=models.ManyToManyField(related_name='repair_work', verbose_name=b'\xd0\xa0\xd0\xb5\xd0\xbc\xd0\xbe\xd0\xbd\xd1\x82', to='service.RepairWork', blank=True),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='serv_work',
            field=models.ManyToManyField(related_name='serv_work', verbose_name=b'\xd0\x9e\xd0\xb1\xd1\x81\xd0\xbb\xd1\x83\xd0\xb6\xd0\xb8\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', to='service.ServWork', blank=True),
        ),
    ]

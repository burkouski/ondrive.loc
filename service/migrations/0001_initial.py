# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0002_auto_20150723_1402'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddServices',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('work_name', models.CharField(max_length=200, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b')),
                ('logo', models.ImageField(upload_to=b'', verbose_name=b'\xd0\xb8\xd0\xba\xd0\xbe\xd0\xbd\xd0\xba\xd0\xb0 \xd1\x83\xd1\x81\xd0\xbb\xd1\x83\xd0\xb3\xd0\xb8', blank=True)),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u0443\u0441\u043b\u0443\u0433\u0438',
            },
        ),
        migrations.CreateModel(
            name='AddWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('work_name', models.CharField(max_length=200, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u0440\u0430\u0431\u043e\u0442\u044b',
            },
        ),
        migrations.CreateModel(
            name='AutoService',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0435\u0440\u0432\u0438\u0441\u0430')),
                ('alias', models.SlugField(max_length=100, blank=True)),
                ('teaser', models.TextField(verbose_name='\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('address', models.CharField(max_length=200, verbose_name='\u0410\u0434\u0440\u0435\u0441', blank=True)),
                ('phone_velcom', models.CharField(max_length=20, verbose_name='Velcom', blank=True)),
                ('phone_velcom2', models.CharField(max_length=20, verbose_name='\u0432\u0442\u043e\u0440\u043e\u0439 Velcom', blank=True)),
                ('phone_mts', models.CharField(max_length=20, verbose_name='\u041c\u0422\u0421', blank=True)),
                ('phone_mts2', models.CharField(max_length=10, verbose_name='\u0432\u0442\u043e\u0440\u043e\u0439 \u041c\u0422\u0421', blank=True)),
                ('phone_life', models.CharField(max_length=20, verbose_name='Life', blank=True)),
                ('phone_life2', models.CharField(max_length=20, verbose_name='\u0432\u0442\u043e\u0440\u043e\u0439 Life', blank=True)),
                ('phone_city', models.CharField(max_length=20, verbose_name='\u0413\u043e\u0440\u043e\u0434\u0441\u043a\u043e\u0439', blank=True)),
                ('phone_city2', models.CharField(max_length=20, verbose_name='\u0432\u0442\u043e\u0440\u043e\u0439 \u0413\u043e\u0440\u043e\u0434\u0441\u043a\u043e\u0439', blank=True)),
                ('work_start', models.CharField(default=b'8', max_length=5, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0440\u0430\u0431\u043e\u0442\u044b', blank=True, choices=[(b'0', b'0:00'), (b'1', b'1:00'), (b'2', b'2:00'), (b'3', b'3:00'), (b'4', b'4:00'), (b'5', b'5:00'), (b'6', b'6:00'), (b'7', b'7:00'), (b'8', b'8:00'), (b'9', b'9:00'), (b'10', b'10:00'), (b'11', b'11:00'), (b'12', b'12:00'), (b'13', b'13:00'), (b'14', b'14:00'), (b'15', b'15:00'), (b'16', b'16:00'), (b'17', b'17:00'), (b'18', b'18:00'), (b'19', b'19:00'), (b'20', b'20:00'), (b'21', b'21:00'), (b'22', b'22:00'), (b'23', b'23:00')])),
                ('work_end', models.CharField(default=b'18', max_length=5, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u0440\u0430\u0431\u043e\u0442\u044b', blank=True, choices=[(b'0', b'0:00'), (b'1', b'1:00'), (b'2', b'2:00'), (b'3', b'3:00'), (b'4', b'4:00'), (b'5', b'5:00'), (b'6', b'6:00'), (b'7', b'7:00'), (b'8', b'8:00'), (b'9', b'9:00'), (b'10', b'10:00'), (b'11', b'11:00'), (b'12', b'12:00'), (b'13', b'13:00'), (b'14', b'14:00'), (b'15', b'15:00'), (b'16', b'16:00'), (b'17', b'17:00'), (b'18', b'18:00'), (b'19', b'19:00'), (b'20', b'20:00'), (b'21', b'21:00'), (b'22', b'22:00'), (b'23', b'23:00')])),
                ('break_time_start', models.CharField(blank=True, max_length=5, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u043e\u0431\u0435\u0434\u0430', choices=[(b'0', b'0:00'), (b'1', b'1:00'), (b'2', b'2:00'), (b'3', b'3:00'), (b'4', b'4:00'), (b'5', b'5:00'), (b'6', b'6:00'), (b'7', b'7:00'), (b'8', b'8:00'), (b'9', b'9:00'), (b'10', b'10:00'), (b'11', b'11:00'), (b'12', b'12:00'), (b'13', b'13:00'), (b'14', b'14:00'), (b'15', b'15:00'), (b'16', b'16:00'), (b'17', b'17:00'), (b'18', b'18:00'), (b'19', b'19:00'), (b'20', b'20:00'), (b'21', b'21:00'), (b'22', b'22:00'), (b'23', b'23:00')])),
                ('break_time_end', models.CharField(blank=True, max_length=5, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u043e\u0431\u0435\u0434\u0430', choices=[(b'0', b'0:00'), (b'1', b'1:00'), (b'2', b'2:00'), (b'3', b'3:00'), (b'4', b'4:00'), (b'5', b'5:00'), (b'6', b'6:00'), (b'7', b'7:00'), (b'8', b'8:00'), (b'9', b'9:00'), (b'10', b'10:00'), (b'11', b'11:00'), (b'12', b'12:00'), (b'13', b'13:00'), (b'14', b'14:00'), (b'15', b'15:00'), (b'16', b'16:00'), (b'17', b'17:00'), (b'18', b'18:00'), (b'19', b'19:00'), (b'20', b'20:00'), (b'21', b'21:00'), (b'22', b'22:00'), (b'23', b'23:00')])),
                ('holiday_time_start', models.CharField(default=b'8', max_length=5, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0441\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u043e\u0433\u043e \u0434\u043d\u044f', blank=True, choices=[(b'0', b'0:00'), (b'1', b'1:00'), (b'2', b'2:00'), (b'3', b'3:00'), (b'4', b'4:00'), (b'5', b'5:00'), (b'6', b'6:00'), (b'7', b'7:00'), (b'8', b'8:00'), (b'9', b'9:00'), (b'10', b'10:00'), (b'11', b'11:00'), (b'12', b'12:00'), (b'13', b'13:00'), (b'14', b'14:00'), (b'15', b'15:00'), (b'16', b'16:00'), (b'17', b'17:00'), (b'18', b'18:00'), (b'19', b'19:00'), (b'20', b'20:00'), (b'21', b'21:00'), (b'22', b'22:00'), (b'23', b'23:00')])),
                ('holiday_time_end', models.CharField(default=b'16', max_length=5, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u0441\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u043e\u0433\u043e \u0434\u043d\u044f', blank=True, choices=[(b'0', b'0:00'), (b'1', b'1:00'), (b'2', b'2:00'), (b'3', b'3:00'), (b'4', b'4:00'), (b'5', b'5:00'), (b'6', b'6:00'), (b'7', b'7:00'), (b'8', b'8:00'), (b'9', b'9:00'), (b'10', b'10:00'), (b'11', b'11:00'), (b'12', b'12:00'), (b'13', b'13:00'), (b'14', b'14:00'), (b'15', b'15:00'), (b'16', b'16:00'), (b'17', b'17:00'), (b'18', b'18:00'), (b'19', b'19:00'), (b'20', b'20:00'), (b'21', b'21:00'), (b'22', b'22:00'), (b'23', b'23:00')])),
                ('monday', models.CharField(default=b'wd', max_length=2, verbose_name='\u041f\u043e\u043d\u0435\u0434\u0435\u043b\u044c\u043d\u0438\u043a', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')])),
                ('tuesday', models.CharField(default=b'wd', max_length=2, verbose_name='\u0412\u0442\u043e\u0440\u043d\u0438\u043a', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')])),
                ('wednesday', models.CharField(default=b'wd', max_length=2, verbose_name='\u0421\u0440\u0435\u0434\u0430', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')])),
                ('thursday', models.CharField(default=b'wd', max_length=2, verbose_name='\u0427\u0435\u0442\u0432\u0435\u0440\u0433', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')])),
                ('friday', models.CharField(default=b'wd', max_length=2, verbose_name='\u041f\u044f\u0442\u043d\u0438\u0446\u0430', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')])),
                ('saturday', models.CharField(default=b'wd', max_length=2, verbose_name='\u0421\u0443\u0431\u0431\u043e\u0442\u0430', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')])),
                ('sunday', models.CharField(default=b'wd', max_length=2, verbose_name='\u0412\u043e\u0441\u043a\u0440\u0435\u0441\u0435\u043d\u044c\u0435', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')])),
                ('email', models.EmailField(max_length=254, verbose_name='Email', blank=True)),
                ('site_url', models.URLField(verbose_name='\u0421\u0430\u0439\u0442', blank=True)),
                ('full_desc', ckeditor.fields.RichTextField(verbose_name='\u041f\u043e\u043b\u043d\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('logo', models.ImageField(upload_to=b'', verbose_name='\u041b\u043e\u0433\u043e\u0442\u0438\u043f \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438', blank=True)),
                ('is_moderate', models.BooleanField(default=False, verbose_name='\u0412\u044b\u0432\u043e\u0434\u0438\u0442\u044c \u0432 \u0442\u043e\u043f \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439?')),
                ('latitude', models.CharField(max_length=200, verbose_name='\u0428\u0438\u0440\u043e\u0442\u0430', blank=True)),
                ('longitude', models.CharField(max_length=200, verbose_name='\u0414\u043e\u043b\u0433\u043e\u0442\u0430', blank=True)),
                ('title', models.CharField(max_length=200, verbose_name='title \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b', blank=True)),
                ('meta_keywords', models.TextField(verbose_name='Keywords', blank=True)),
                ('meta_description', models.TextField(null=True, verbose_name='Description', blank=True)),
                ('add_services', models.ManyToManyField(related_name='autoservice_add_services', verbose_name='\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u0443\u0441\u043b\u0443\u0433\u0438', to='service.AddServices', blank=True)),
                ('add_work', models.ManyToManyField(related_name='add_work', verbose_name='\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u0440\u0430\u0431\u043e\u0442\u044b', to='service.AddWork', blank=True)),
            ],
            options={
                'verbose_name': '\u0410\u0432\u0442\u043e\u0441\u0435\u0440\u0432\u0438\u0441',
                'verbose_name_plural': '\u0410\u0432\u0442\u043e\u0441\u0435\u0440\u0432\u0438\u0441\u044b',
            },
        ),
        migrations.CreateModel(
            name='CarWash',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0435\u0440\u0432\u0438\u0441\u0430')),
                ('alias', models.SlugField(max_length=100, blank=True)),
                ('teaser', models.TextField(verbose_name='\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('address', models.CharField(max_length=200, verbose_name='\u0410\u0434\u0440\u0435\u0441', blank=True)),
                ('phone_velcom', models.CharField(max_length=20, verbose_name='Velcom', blank=True)),
                ('phone_velcom2', models.CharField(max_length=20, verbose_name='\u0432\u0442\u043e\u0440\u043e\u0439 Velcom', blank=True)),
                ('phone_mts', models.CharField(max_length=20, verbose_name='\u041c\u0422\u0421', blank=True)),
                ('phone_mts2', models.CharField(max_length=10, verbose_name='\u0432\u0442\u043e\u0440\u043e\u0439 \u041c\u0422\u0421', blank=True)),
                ('phone_life', models.CharField(max_length=20, verbose_name='Life', blank=True)),
                ('phone_life2', models.CharField(max_length=20, verbose_name='\u0432\u0442\u043e\u0440\u043e\u0439 Life', blank=True)),
                ('phone_city', models.CharField(max_length=20, verbose_name='\u0413\u043e\u0440\u043e\u0434\u0441\u043a\u043e\u0439', blank=True)),
                ('phone_city2', models.CharField(max_length=20, verbose_name='\u0432\u0442\u043e\u0440\u043e\u0439 \u0413\u043e\u0440\u043e\u0434\u0441\u043a\u043e\u0439', blank=True)),
                ('work_start', models.CharField(default=b'8', max_length=5, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0440\u0430\u0431\u043e\u0442\u044b', blank=True, choices=[(b'0', b'0:00'), (b'1', b'1:00'), (b'2', b'2:00'), (b'3', b'3:00'), (b'4', b'4:00'), (b'5', b'5:00'), (b'6', b'6:00'), (b'7', b'7:00'), (b'8', b'8:00'), (b'9', b'9:00'), (b'10', b'10:00'), (b'11', b'11:00'), (b'12', b'12:00'), (b'13', b'13:00'), (b'14', b'14:00'), (b'15', b'15:00'), (b'16', b'16:00'), (b'17', b'17:00'), (b'18', b'18:00'), (b'19', b'19:00'), (b'20', b'20:00'), (b'21', b'21:00'), (b'22', b'22:00'), (b'23', b'23:00')])),
                ('work_end', models.CharField(default=b'18', max_length=5, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u0440\u0430\u0431\u043e\u0442\u044b', blank=True, choices=[(b'0', b'0:00'), (b'1', b'1:00'), (b'2', b'2:00'), (b'3', b'3:00'), (b'4', b'4:00'), (b'5', b'5:00'), (b'6', b'6:00'), (b'7', b'7:00'), (b'8', b'8:00'), (b'9', b'9:00'), (b'10', b'10:00'), (b'11', b'11:00'), (b'12', b'12:00'), (b'13', b'13:00'), (b'14', b'14:00'), (b'15', b'15:00'), (b'16', b'16:00'), (b'17', b'17:00'), (b'18', b'18:00'), (b'19', b'19:00'), (b'20', b'20:00'), (b'21', b'21:00'), (b'22', b'22:00'), (b'23', b'23:00')])),
                ('break_time_start', models.CharField(blank=True, max_length=5, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u043e\u0431\u0435\u0434\u0430', choices=[(b'0', b'0:00'), (b'1', b'1:00'), (b'2', b'2:00'), (b'3', b'3:00'), (b'4', b'4:00'), (b'5', b'5:00'), (b'6', b'6:00'), (b'7', b'7:00'), (b'8', b'8:00'), (b'9', b'9:00'), (b'10', b'10:00'), (b'11', b'11:00'), (b'12', b'12:00'), (b'13', b'13:00'), (b'14', b'14:00'), (b'15', b'15:00'), (b'16', b'16:00'), (b'17', b'17:00'), (b'18', b'18:00'), (b'19', b'19:00'), (b'20', b'20:00'), (b'21', b'21:00'), (b'22', b'22:00'), (b'23', b'23:00')])),
                ('break_time_end', models.CharField(blank=True, max_length=5, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u043e\u0431\u0435\u0434\u0430', choices=[(b'0', b'0:00'), (b'1', b'1:00'), (b'2', b'2:00'), (b'3', b'3:00'), (b'4', b'4:00'), (b'5', b'5:00'), (b'6', b'6:00'), (b'7', b'7:00'), (b'8', b'8:00'), (b'9', b'9:00'), (b'10', b'10:00'), (b'11', b'11:00'), (b'12', b'12:00'), (b'13', b'13:00'), (b'14', b'14:00'), (b'15', b'15:00'), (b'16', b'16:00'), (b'17', b'17:00'), (b'18', b'18:00'), (b'19', b'19:00'), (b'20', b'20:00'), (b'21', b'21:00'), (b'22', b'22:00'), (b'23', b'23:00')])),
                ('holiday_time_start', models.CharField(default=b'8', max_length=5, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0441\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u043e\u0433\u043e \u0434\u043d\u044f', blank=True, choices=[(b'0', b'0:00'), (b'1', b'1:00'), (b'2', b'2:00'), (b'3', b'3:00'), (b'4', b'4:00'), (b'5', b'5:00'), (b'6', b'6:00'), (b'7', b'7:00'), (b'8', b'8:00'), (b'9', b'9:00'), (b'10', b'10:00'), (b'11', b'11:00'), (b'12', b'12:00'), (b'13', b'13:00'), (b'14', b'14:00'), (b'15', b'15:00'), (b'16', b'16:00'), (b'17', b'17:00'), (b'18', b'18:00'), (b'19', b'19:00'), (b'20', b'20:00'), (b'21', b'21:00'), (b'22', b'22:00'), (b'23', b'23:00')])),
                ('holiday_time_end', models.CharField(default=b'16', max_length=5, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u0441\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u043e\u0433\u043e \u0434\u043d\u044f', blank=True, choices=[(b'0', b'0:00'), (b'1', b'1:00'), (b'2', b'2:00'), (b'3', b'3:00'), (b'4', b'4:00'), (b'5', b'5:00'), (b'6', b'6:00'), (b'7', b'7:00'), (b'8', b'8:00'), (b'9', b'9:00'), (b'10', b'10:00'), (b'11', b'11:00'), (b'12', b'12:00'), (b'13', b'13:00'), (b'14', b'14:00'), (b'15', b'15:00'), (b'16', b'16:00'), (b'17', b'17:00'), (b'18', b'18:00'), (b'19', b'19:00'), (b'20', b'20:00'), (b'21', b'21:00'), (b'22', b'22:00'), (b'23', b'23:00')])),
                ('monday', models.CharField(default=b'wd', max_length=2, verbose_name='\u041f\u043e\u043d\u0435\u0434\u0435\u043b\u044c\u043d\u0438\u043a', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')])),
                ('tuesday', models.CharField(default=b'wd', max_length=2, verbose_name='\u0412\u0442\u043e\u0440\u043d\u0438\u043a', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')])),
                ('wednesday', models.CharField(default=b'wd', max_length=2, verbose_name='\u0421\u0440\u0435\u0434\u0430', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')])),
                ('thursday', models.CharField(default=b'wd', max_length=2, verbose_name='\u0427\u0435\u0442\u0432\u0435\u0440\u0433', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')])),
                ('friday', models.CharField(default=b'wd', max_length=2, verbose_name='\u041f\u044f\u0442\u043d\u0438\u0446\u0430', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')])),
                ('saturday', models.CharField(default=b'wd', max_length=2, verbose_name='\u0421\u0443\u0431\u0431\u043e\u0442\u0430', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')])),
                ('sunday', models.CharField(default=b'wd', max_length=2, verbose_name='\u0412\u043e\u0441\u043a\u0440\u0435\u0441\u0435\u043d\u044c\u0435', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')])),
                ('email', models.EmailField(max_length=254, verbose_name='Email', blank=True)),
                ('site_url', models.URLField(verbose_name='\u0421\u0430\u0439\u0442', blank=True)),
                ('full_desc', ckeditor.fields.RichTextField(verbose_name='\u041f\u043e\u043b\u043d\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('logo', models.ImageField(upload_to=b'', verbose_name='\u041b\u043e\u0433\u043e\u0442\u0438\u043f \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438', blank=True)),
                ('is_moderate', models.BooleanField(default=False, verbose_name='\u0412\u044b\u0432\u043e\u0434\u0438\u0442\u044c \u0432 \u0442\u043e\u043f \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439?')),
                ('latitude', models.CharField(max_length=200, verbose_name='\u0428\u0438\u0440\u043e\u0442\u0430', blank=True)),
                ('longitude', models.CharField(max_length=200, verbose_name='\u0414\u043e\u043b\u0433\u043e\u0442\u0430', blank=True)),
                ('title', models.CharField(max_length=200, verbose_name='title \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b', blank=True)),
                ('meta_keywords', models.TextField(verbose_name='Keywords', blank=True)),
                ('meta_description', models.TextField(null=True, verbose_name='Description', blank=True)),
                ('add_services', models.ManyToManyField(related_name='carwash_add_services', verbose_name=b'\xd0\x94\xd0\xbe\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x8b\xd0\xb5 \xd1\x83\xd1\x81\xd0\xbb\xd1\x83\xd0\xb3\xd0\xb8', to='service.AddServices', blank=True)),
            ],
            options={
                'verbose_name': '\u0410\u0432\u0442\u043e\u043c\u043e\u0439\u043a\u0430',
                'verbose_name_plural': '\u0410\u0432\u0442\u043e\u043c\u043e\u0439\u043a\u0438',
            },
        ),
        migrations.CreateModel(
            name='CarWashServices',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('work_name', models.CharField(max_length=200, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '\u0423\u0441\u043b\u0443\u0433\u0438',
            },
        ),
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
            name='DiscWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('work_name', models.CharField(max_length=200, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '\u0414\u0438\u0441\u043a\u0438',
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
        migrations.CreateModel(
            name='SpecializationWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('work_name', models.CharField(max_length=200, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b')),
                ('logo', models.ImageField(upload_to=b'', verbose_name=b'\xd0\x9b\xd0\xbe\xd0\xb3\xd0\xbe\xd1\x82\xd0\xb8\xd0\xbf \xd0\xbc\xd0\xb0\xd1\x80\xd0\xba\xd0\xb8', blank=True)),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0437\u0438\u0440\u0443\u044e\u0442\u0441\u044f \u043d\u0430 \u043c\u0430\u0440\u043a\u0430\u0445',
            },
        ),
        migrations.CreateModel(
            name='TireService',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0435\u0440\u0432\u0438\u0441\u0430')),
                ('alias', models.SlugField(max_length=100, blank=True)),
                ('teaser', models.TextField(verbose_name='\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('address', models.CharField(max_length=200, verbose_name='\u0410\u0434\u0440\u0435\u0441', blank=True)),
                ('phone_velcom', models.CharField(max_length=20, verbose_name='Velcom', blank=True)),
                ('phone_velcom2', models.CharField(max_length=20, verbose_name='\u0432\u0442\u043e\u0440\u043e\u0439 Velcom', blank=True)),
                ('phone_mts', models.CharField(max_length=20, verbose_name='\u041c\u0422\u0421', blank=True)),
                ('phone_mts2', models.CharField(max_length=10, verbose_name='\u0432\u0442\u043e\u0440\u043e\u0439 \u041c\u0422\u0421', blank=True)),
                ('phone_life', models.CharField(max_length=20, verbose_name='Life', blank=True)),
                ('phone_life2', models.CharField(max_length=20, verbose_name='\u0432\u0442\u043e\u0440\u043e\u0439 Life', blank=True)),
                ('phone_city', models.CharField(max_length=20, verbose_name='\u0413\u043e\u0440\u043e\u0434\u0441\u043a\u043e\u0439', blank=True)),
                ('phone_city2', models.CharField(max_length=20, verbose_name='\u0432\u0442\u043e\u0440\u043e\u0439 \u0413\u043e\u0440\u043e\u0434\u0441\u043a\u043e\u0439', blank=True)),
                ('work_start', models.CharField(default=b'8', max_length=5, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0440\u0430\u0431\u043e\u0442\u044b', blank=True, choices=[(b'0', b'0:00'), (b'1', b'1:00'), (b'2', b'2:00'), (b'3', b'3:00'), (b'4', b'4:00'), (b'5', b'5:00'), (b'6', b'6:00'), (b'7', b'7:00'), (b'8', b'8:00'), (b'9', b'9:00'), (b'10', b'10:00'), (b'11', b'11:00'), (b'12', b'12:00'), (b'13', b'13:00'), (b'14', b'14:00'), (b'15', b'15:00'), (b'16', b'16:00'), (b'17', b'17:00'), (b'18', b'18:00'), (b'19', b'19:00'), (b'20', b'20:00'), (b'21', b'21:00'), (b'22', b'22:00'), (b'23', b'23:00')])),
                ('work_end', models.CharField(default=b'18', max_length=5, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u0440\u0430\u0431\u043e\u0442\u044b', blank=True, choices=[(b'0', b'0:00'), (b'1', b'1:00'), (b'2', b'2:00'), (b'3', b'3:00'), (b'4', b'4:00'), (b'5', b'5:00'), (b'6', b'6:00'), (b'7', b'7:00'), (b'8', b'8:00'), (b'9', b'9:00'), (b'10', b'10:00'), (b'11', b'11:00'), (b'12', b'12:00'), (b'13', b'13:00'), (b'14', b'14:00'), (b'15', b'15:00'), (b'16', b'16:00'), (b'17', b'17:00'), (b'18', b'18:00'), (b'19', b'19:00'), (b'20', b'20:00'), (b'21', b'21:00'), (b'22', b'22:00'), (b'23', b'23:00')])),
                ('break_time_start', models.CharField(blank=True, max_length=5, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u043e\u0431\u0435\u0434\u0430', choices=[(b'0', b'0:00'), (b'1', b'1:00'), (b'2', b'2:00'), (b'3', b'3:00'), (b'4', b'4:00'), (b'5', b'5:00'), (b'6', b'6:00'), (b'7', b'7:00'), (b'8', b'8:00'), (b'9', b'9:00'), (b'10', b'10:00'), (b'11', b'11:00'), (b'12', b'12:00'), (b'13', b'13:00'), (b'14', b'14:00'), (b'15', b'15:00'), (b'16', b'16:00'), (b'17', b'17:00'), (b'18', b'18:00'), (b'19', b'19:00'), (b'20', b'20:00'), (b'21', b'21:00'), (b'22', b'22:00'), (b'23', b'23:00')])),
                ('break_time_end', models.CharField(blank=True, max_length=5, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u043e\u0431\u0435\u0434\u0430', choices=[(b'0', b'0:00'), (b'1', b'1:00'), (b'2', b'2:00'), (b'3', b'3:00'), (b'4', b'4:00'), (b'5', b'5:00'), (b'6', b'6:00'), (b'7', b'7:00'), (b'8', b'8:00'), (b'9', b'9:00'), (b'10', b'10:00'), (b'11', b'11:00'), (b'12', b'12:00'), (b'13', b'13:00'), (b'14', b'14:00'), (b'15', b'15:00'), (b'16', b'16:00'), (b'17', b'17:00'), (b'18', b'18:00'), (b'19', b'19:00'), (b'20', b'20:00'), (b'21', b'21:00'), (b'22', b'22:00'), (b'23', b'23:00')])),
                ('holiday_time_start', models.CharField(default=b'8', max_length=5, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0441\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u043e\u0433\u043e \u0434\u043d\u044f', blank=True, choices=[(b'0', b'0:00'), (b'1', b'1:00'), (b'2', b'2:00'), (b'3', b'3:00'), (b'4', b'4:00'), (b'5', b'5:00'), (b'6', b'6:00'), (b'7', b'7:00'), (b'8', b'8:00'), (b'9', b'9:00'), (b'10', b'10:00'), (b'11', b'11:00'), (b'12', b'12:00'), (b'13', b'13:00'), (b'14', b'14:00'), (b'15', b'15:00'), (b'16', b'16:00'), (b'17', b'17:00'), (b'18', b'18:00'), (b'19', b'19:00'), (b'20', b'20:00'), (b'21', b'21:00'), (b'22', b'22:00'), (b'23', b'23:00')])),
                ('holiday_time_end', models.CharField(default=b'16', max_length=5, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u0441\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u043e\u0433\u043e \u0434\u043d\u044f', blank=True, choices=[(b'0', b'0:00'), (b'1', b'1:00'), (b'2', b'2:00'), (b'3', b'3:00'), (b'4', b'4:00'), (b'5', b'5:00'), (b'6', b'6:00'), (b'7', b'7:00'), (b'8', b'8:00'), (b'9', b'9:00'), (b'10', b'10:00'), (b'11', b'11:00'), (b'12', b'12:00'), (b'13', b'13:00'), (b'14', b'14:00'), (b'15', b'15:00'), (b'16', b'16:00'), (b'17', b'17:00'), (b'18', b'18:00'), (b'19', b'19:00'), (b'20', b'20:00'), (b'21', b'21:00'), (b'22', b'22:00'), (b'23', b'23:00')])),
                ('monday', models.CharField(default=b'wd', max_length=2, verbose_name='\u041f\u043e\u043d\u0435\u0434\u0435\u043b\u044c\u043d\u0438\u043a', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')])),
                ('tuesday', models.CharField(default=b'wd', max_length=2, verbose_name='\u0412\u0442\u043e\u0440\u043d\u0438\u043a', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')])),
                ('wednesday', models.CharField(default=b'wd', max_length=2, verbose_name='\u0421\u0440\u0435\u0434\u0430', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')])),
                ('thursday', models.CharField(default=b'wd', max_length=2, verbose_name='\u0427\u0435\u0442\u0432\u0435\u0440\u0433', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')])),
                ('friday', models.CharField(default=b'wd', max_length=2, verbose_name='\u041f\u044f\u0442\u043d\u0438\u0446\u0430', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')])),
                ('saturday', models.CharField(default=b'wd', max_length=2, verbose_name='\u0421\u0443\u0431\u0431\u043e\u0442\u0430', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')])),
                ('sunday', models.CharField(default=b'wd', max_length=2, verbose_name='\u0412\u043e\u0441\u043a\u0440\u0435\u0441\u0435\u043d\u044c\u0435', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')])),
                ('email', models.EmailField(max_length=254, verbose_name='Email', blank=True)),
                ('site_url', models.URLField(verbose_name='\u0421\u0430\u0439\u0442', blank=True)),
                ('full_desc', ckeditor.fields.RichTextField(verbose_name='\u041f\u043e\u043b\u043d\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('logo', models.ImageField(upload_to=b'', verbose_name='\u041b\u043e\u0433\u043e\u0442\u0438\u043f \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438', blank=True)),
                ('is_moderate', models.BooleanField(default=False, verbose_name='\u0412\u044b\u0432\u043e\u0434\u0438\u0442\u044c \u0432 \u0442\u043e\u043f \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439?')),
                ('latitude', models.CharField(max_length=200, verbose_name='\u0428\u0438\u0440\u043e\u0442\u0430', blank=True)),
                ('longitude', models.CharField(max_length=200, verbose_name='\u0414\u043e\u043b\u0433\u043e\u0442\u0430', blank=True)),
                ('title', models.CharField(max_length=200, verbose_name='title \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b', blank=True)),
                ('meta_keywords', models.TextField(verbose_name='Keywords', blank=True)),
                ('meta_description', models.TextField(null=True, verbose_name='Description', blank=True)),
                ('add_services', models.ManyToManyField(related_name='tire_add_services', verbose_name=b'\xd0\x94\xd0\xbe\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x8b\xd0\xb5 \xd1\x83\xd1\x81\xd0\xbb\xd1\x83\xd0\xb3\xd0\xb8', to='service.AddServices', blank=True)),
                ('disc_work', models.ManyToManyField(related_name='disc_work', verbose_name=b'\xd0\x94\xd0\xb8\xd1\x81\xd0\xba\xd0\xb8', to='service.DiscWork', blank=True)),
                ('owner', models.ForeignKey(default=b'85', to='myauth.UserProfile')),
            ],
            options={
                'verbose_name': '\u0428\u0438\u043d\u043e\u043c\u043e\u043d\u0442\u0430\u0436',
                'verbose_name_plural': '\u0428\u0438\u043d\u043e\u043c\u043e\u043d\u0442\u0430\u0436\u0438',
            },
        ),
        migrations.CreateModel(
            name='TireWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('work_name', models.CharField(max_length=200, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '\u0428\u0438\u043d\u044b',
            },
        ),
        migrations.CreateModel(
            name='TypeCarWash',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('work_name', models.CharField(max_length=200, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '\u0412\u0438\u0434 \u043c\u043e\u0439\u043a\u0438',
            },
        ),
        migrations.CreateModel(
            name='TypeVehicle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('work_name', models.CharField(max_length=200, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '\u0412\u0438\u0434 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0430',
            },
        ),
        migrations.AddField(
            model_name='tireservice',
            name='tire_work',
            field=models.ManyToManyField(related_name='tire_work', verbose_name=b'\xd0\xa8\xd0\xb8\xd0\xbd\xd1\x8b', to='service.TireWork', blank=True),
        ),
        migrations.AddField(
            model_name='carwash',
            name='car_wash_services',
            field=models.ManyToManyField(related_name='car_wash_services', verbose_name=b'\xd0\xa3\xd1\x81\xd0\xbb\xd1\x83\xd0\xb3\xd0\xb8', to='service.CarWashServices', blank=True),
        ),
        migrations.AddField(
            model_name='carwash',
            name='owner',
            field=models.ForeignKey(default=b'85', to='myauth.UserProfile'),
        ),
        migrations.AddField(
            model_name='carwash',
            name='type_carwash',
            field=models.ManyToManyField(related_name='type_carwash', verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd0\xbc\xd0\xbe\xd0\xb9\xd0\xba\xd0\xb8', to='service.TypeCarWash', blank=True),
        ),
        migrations.AddField(
            model_name='carwash',
            name='type_vehicle',
            field=models.ManyToManyField(related_name='type_vehicle', verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd1\x82\xd1\x80\xd0\xb0\xd0\xbd\xd1\x81\xd0\xbf\xd0\xbe\xd1\x80\xd1\x82\xd0\xb0', to='service.TypeVehicle', blank=True),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='diag_work',
            field=models.ManyToManyField(related_name='diag_work', verbose_name='\u0414\u0438\u0430\u0433\u043d\u043e\u0441\u0442\u0438\u043a\u0430', to='service.DiagWork', blank=True),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='owner',
            field=models.ForeignKey(default=b'85', to='myauth.UserProfile'),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='repair_work',
            field=models.ManyToManyField(related_name='repair_work', verbose_name='\u0420\u0435\u043c\u043e\u043d\u0442', to='service.RepairWork', blank=True),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='serv_work',
            field=models.ManyToManyField(related_name='serv_work', verbose_name='\u041e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u043d\u0438\u0435', to='service.ServWork', blank=True),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='specialization_work',
            field=models.ManyToManyField(related_name='specialization_work', verbose_name='\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0437\u0438\u0440\u0443\u044e\u0449\u0438\u0435\u0441\u044f \u043d\u0430 \u043c\u0430\u0440\u043a\u0435', to='service.SpecializationWork', blank=True),
        ),
    ]

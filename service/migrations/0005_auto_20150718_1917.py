# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_auto_20150718_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='autoservice',
            name='address',
            field=models.CharField(max_length=200, verbose_name='\u0410\u0434\u0440\u0435\u0441', blank=True),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='alias',
            field=models.SlugField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='break_time_end',
            field=models.TimeField(null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u043e\u0431\u0435\u0434\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='break_time_start',
            field=models.TimeField(null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u043e\u0431\u0435\u0434\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email', blank=True),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='friday',
            field=models.CharField(default=b'wd', max_length=2, verbose_name='\u041f\u044f\u0442\u043d\u0438\u0446\u0430', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')]),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='full_desc',
            field=ckeditor.fields.RichTextField(verbose_name='\u041f\u043e\u043b\u043d\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='holiday',
            field=models.CharField(max_length=10, verbose_name='\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0435 \u0434\u043d\u0438', blank=True),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='holiday_time_end',
            field=models.TimeField(null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u0441\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u043e\u0433\u043e \u0434\u043d\u044f', blank=True),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='holiday_time_start',
            field=models.TimeField(null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0441\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u043e\u0433\u043e \u0434\u043d\u044f', blank=True),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='is_top',
            field=models.BooleanField(default=None, verbose_name='\u0412\u044b\u0432\u043e\u0434\u0438\u0442\u044c \u0432 \u0442\u043e\u043f \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439?'),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='latitude',
            field=models.CharField(max_length=200, verbose_name='\u0428\u0438\u0440\u043e\u0442\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='logo',
            field=models.ImageField(upload_to=b'', verbose_name='\u041b\u043e\u0433\u043e\u0442\u0438\u043f \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438', blank=True),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='longitude',
            field=models.CharField(max_length=200, verbose_name='\u0414\u043e\u043b\u0433\u043e\u0442\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='meta_description',
            field=models.TextField(null=True, verbose_name='Description', blank=True),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='meta_keywords',
            field=models.TextField(verbose_name='Keywords', blank=True),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='monday',
            field=models.CharField(default=b'wd', max_length=2, verbose_name='\u041f\u043e\u043d\u0435\u0434\u0435\u043b\u044c\u043d\u0438\u043a', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')]),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='phone_city',
            field=models.CharField(max_length=20, verbose_name='\u0413\u043e\u0440\u043e\u0434\u0441\u043a\u043e\u0439', blank=True),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='phone_city2',
            field=models.CharField(max_length=20, verbose_name='\u0432\u0442\u043e\u0440\u043e\u0439 \u0413\u043e\u0440\u043e\u0434\u0441\u043a\u043e\u0439', blank=True),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='phone_life',
            field=models.CharField(max_length=20, verbose_name='Life', blank=True),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='phone_life2',
            field=models.CharField(max_length=20, verbose_name='\u0432\u0442\u043e\u0440\u043e\u0439 Life', blank=True),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='phone_mts',
            field=models.CharField(max_length=20, verbose_name='\u041c\u0422\u0421', blank=True),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='phone_mts2',
            field=models.CharField(max_length=10, verbose_name='\u0432\u0442\u043e\u0440\u043e\u0439 \u041c\u0422\u0421', blank=True),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='phone_velcom',
            field=models.CharField(max_length=20, verbose_name='Velcom', blank=True),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='phone_velcom2',
            field=models.CharField(max_length=20, verbose_name='\u0432\u0442\u043e\u0440\u043e\u0439 Velcom', blank=True),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='saturday',
            field=models.CharField(default=b'wd', max_length=2, verbose_name='\u0421\u0443\u0431\u0431\u043e\u0442\u0430', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')]),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='site_url',
            field=models.URLField(verbose_name='\u0421\u0430\u0439\u0442', blank=True),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='sunday',
            field=models.CharField(default=b'wd', max_length=2, verbose_name='\u0412\u043e\u0441\u043a\u0440\u0435\u0441\u0435\u043d\u044c\u0435', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')]),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='teaser',
            field=models.TextField(verbose_name='\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='thursday',
            field=models.CharField(default=b'wd', max_length=2, verbose_name='\u0427\u0435\u0442\u0432\u0435\u0440\u0433', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')]),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='title',
            field=models.CharField(max_length=200, verbose_name='title \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b', blank=True),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='tuesday',
            field=models.CharField(default=b'wd', max_length=2, verbose_name='\u0412\u0442\u043e\u0440\u043d\u0438\u043a', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')]),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='wednesday',
            field=models.CharField(default=b'wd', max_length=2, verbose_name='\u0421\u0440\u0435\u0434\u0430', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')]),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='work_end',
            field=models.TimeField(null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u0440\u0430\u0431\u043e\u0442\u044b', blank=True),
        ),
        migrations.AddField(
            model_name='autoservice',
            name='work_start',
            field=models.TimeField(null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0440\u0430\u0431\u043e\u0442\u044b', blank=True),
        ),
        migrations.AddField(
            model_name='carwash',
            name='address',
            field=models.CharField(max_length=200, verbose_name='\u0410\u0434\u0440\u0435\u0441', blank=True),
        ),
        migrations.AddField(
            model_name='carwash',
            name='alias',
            field=models.SlugField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='carwash',
            name='break_time_end',
            field=models.TimeField(null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u043e\u0431\u0435\u0434\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='carwash',
            name='break_time_start',
            field=models.TimeField(null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u043e\u0431\u0435\u0434\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='carwash',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email', blank=True),
        ),
        migrations.AddField(
            model_name='carwash',
            name='friday',
            field=models.CharField(default=b'wd', max_length=2, verbose_name='\u041f\u044f\u0442\u043d\u0438\u0446\u0430', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')]),
        ),
        migrations.AddField(
            model_name='carwash',
            name='full_desc',
            field=ckeditor.fields.RichTextField(verbose_name='\u041f\u043e\u043b\u043d\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AddField(
            model_name='carwash',
            name='holiday',
            field=models.CharField(max_length=10, verbose_name='\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0435 \u0434\u043d\u0438', blank=True),
        ),
        migrations.AddField(
            model_name='carwash',
            name='holiday_time_end',
            field=models.TimeField(null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u0441\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u043e\u0433\u043e \u0434\u043d\u044f', blank=True),
        ),
        migrations.AddField(
            model_name='carwash',
            name='holiday_time_start',
            field=models.TimeField(null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0441\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u043e\u0433\u043e \u0434\u043d\u044f', blank=True),
        ),
        migrations.AddField(
            model_name='carwash',
            name='is_top',
            field=models.BooleanField(default=None, verbose_name='\u0412\u044b\u0432\u043e\u0434\u0438\u0442\u044c \u0432 \u0442\u043e\u043f \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439?'),
        ),
        migrations.AddField(
            model_name='carwash',
            name='latitude',
            field=models.CharField(max_length=200, verbose_name='\u0428\u0438\u0440\u043e\u0442\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='carwash',
            name='logo',
            field=models.ImageField(upload_to=b'', verbose_name='\u041b\u043e\u0433\u043e\u0442\u0438\u043f \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438', blank=True),
        ),
        migrations.AddField(
            model_name='carwash',
            name='longitude',
            field=models.CharField(max_length=200, verbose_name='\u0414\u043e\u043b\u0433\u043e\u0442\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='carwash',
            name='meta_description',
            field=models.TextField(null=True, verbose_name='Description', blank=True),
        ),
        migrations.AddField(
            model_name='carwash',
            name='meta_keywords',
            field=models.TextField(verbose_name='Keywords', blank=True),
        ),
        migrations.AddField(
            model_name='carwash',
            name='monday',
            field=models.CharField(default=b'wd', max_length=2, verbose_name='\u041f\u043e\u043d\u0435\u0434\u0435\u043b\u044c\u043d\u0438\u043a', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')]),
        ),
        migrations.AddField(
            model_name='carwash',
            name='phone_city',
            field=models.CharField(max_length=20, verbose_name='\u0413\u043e\u0440\u043e\u0434\u0441\u043a\u043e\u0439', blank=True),
        ),
        migrations.AddField(
            model_name='carwash',
            name='phone_city2',
            field=models.CharField(max_length=20, verbose_name='\u0432\u0442\u043e\u0440\u043e\u0439 \u0413\u043e\u0440\u043e\u0434\u0441\u043a\u043e\u0439', blank=True),
        ),
        migrations.AddField(
            model_name='carwash',
            name='phone_life',
            field=models.CharField(max_length=20, verbose_name='Life', blank=True),
        ),
        migrations.AddField(
            model_name='carwash',
            name='phone_life2',
            field=models.CharField(max_length=20, verbose_name='\u0432\u0442\u043e\u0440\u043e\u0439 Life', blank=True),
        ),
        migrations.AddField(
            model_name='carwash',
            name='phone_mts',
            field=models.CharField(max_length=20, verbose_name='\u041c\u0422\u0421', blank=True),
        ),
        migrations.AddField(
            model_name='carwash',
            name='phone_mts2',
            field=models.CharField(max_length=10, verbose_name='\u0432\u0442\u043e\u0440\u043e\u0439 \u041c\u0422\u0421', blank=True),
        ),
        migrations.AddField(
            model_name='carwash',
            name='phone_velcom',
            field=models.CharField(max_length=20, verbose_name='Velcom', blank=True),
        ),
        migrations.AddField(
            model_name='carwash',
            name='phone_velcom2',
            field=models.CharField(max_length=20, verbose_name='\u0432\u0442\u043e\u0440\u043e\u0439 Velcom', blank=True),
        ),
        migrations.AddField(
            model_name='carwash',
            name='saturday',
            field=models.CharField(default=b'wd', max_length=2, verbose_name='\u0421\u0443\u0431\u0431\u043e\u0442\u0430', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')]),
        ),
        migrations.AddField(
            model_name='carwash',
            name='site_url',
            field=models.URLField(verbose_name='\u0421\u0430\u0439\u0442', blank=True),
        ),
        migrations.AddField(
            model_name='carwash',
            name='sunday',
            field=models.CharField(default=b'wd', max_length=2, verbose_name='\u0412\u043e\u0441\u043a\u0440\u0435\u0441\u0435\u043d\u044c\u0435', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')]),
        ),
        migrations.AddField(
            model_name='carwash',
            name='teaser',
            field=models.TextField(verbose_name='\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AddField(
            model_name='carwash',
            name='thursday',
            field=models.CharField(default=b'wd', max_length=2, verbose_name='\u0427\u0435\u0442\u0432\u0435\u0440\u0433', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')]),
        ),
        migrations.AddField(
            model_name='carwash',
            name='title',
            field=models.CharField(max_length=200, verbose_name='title \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b', blank=True),
        ),
        migrations.AddField(
            model_name='carwash',
            name='tuesday',
            field=models.CharField(default=b'wd', max_length=2, verbose_name='\u0412\u0442\u043e\u0440\u043d\u0438\u043a', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')]),
        ),
        migrations.AddField(
            model_name='carwash',
            name='wednesday',
            field=models.CharField(default=b'wd', max_length=2, verbose_name='\u0421\u0440\u0435\u0434\u0430', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')]),
        ),
        migrations.AddField(
            model_name='carwash',
            name='work_end',
            field=models.TimeField(null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u0440\u0430\u0431\u043e\u0442\u044b', blank=True),
        ),
        migrations.AddField(
            model_name='carwash',
            name='work_start',
            field=models.TimeField(null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0440\u0430\u0431\u043e\u0442\u044b', blank=True),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='address',
            field=models.CharField(max_length=200, verbose_name='\u0410\u0434\u0440\u0435\u0441', blank=True),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='alias',
            field=models.SlugField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='break_time_end',
            field=models.TimeField(null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u043e\u0431\u0435\u0434\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='break_time_start',
            field=models.TimeField(null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u043e\u0431\u0435\u0434\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email', blank=True),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='friday',
            field=models.CharField(default=b'wd', max_length=2, verbose_name='\u041f\u044f\u0442\u043d\u0438\u0446\u0430', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')]),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='full_desc',
            field=ckeditor.fields.RichTextField(verbose_name='\u041f\u043e\u043b\u043d\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='holiday',
            field=models.CharField(max_length=10, verbose_name='\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0435 \u0434\u043d\u0438', blank=True),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='holiday_time_end',
            field=models.TimeField(null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u0441\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u043e\u0433\u043e \u0434\u043d\u044f', blank=True),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='holiday_time_start',
            field=models.TimeField(null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0441\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u043e\u0433\u043e \u0434\u043d\u044f', blank=True),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='is_top',
            field=models.BooleanField(default=None, verbose_name='\u0412\u044b\u0432\u043e\u0434\u0438\u0442\u044c \u0432 \u0442\u043e\u043f \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439?'),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='latitude',
            field=models.CharField(max_length=200, verbose_name='\u0428\u0438\u0440\u043e\u0442\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='logo',
            field=models.ImageField(upload_to=b'', verbose_name='\u041b\u043e\u0433\u043e\u0442\u0438\u043f \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438', blank=True),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='longitude',
            field=models.CharField(max_length=200, verbose_name='\u0414\u043e\u043b\u0433\u043e\u0442\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='meta_description',
            field=models.TextField(null=True, verbose_name='Description', blank=True),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='meta_keywords',
            field=models.TextField(verbose_name='Keywords', blank=True),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='monday',
            field=models.CharField(default=b'wd', max_length=2, verbose_name='\u041f\u043e\u043d\u0435\u0434\u0435\u043b\u044c\u043d\u0438\u043a', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')]),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='phone_city',
            field=models.CharField(max_length=20, verbose_name='\u0413\u043e\u0440\u043e\u0434\u0441\u043a\u043e\u0439', blank=True),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='phone_city2',
            field=models.CharField(max_length=20, verbose_name='\u0432\u0442\u043e\u0440\u043e\u0439 \u0413\u043e\u0440\u043e\u0434\u0441\u043a\u043e\u0439', blank=True),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='phone_life',
            field=models.CharField(max_length=20, verbose_name='Life', blank=True),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='phone_life2',
            field=models.CharField(max_length=20, verbose_name='\u0432\u0442\u043e\u0440\u043e\u0439 Life', blank=True),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='phone_mts',
            field=models.CharField(max_length=20, verbose_name='\u041c\u0422\u0421', blank=True),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='phone_mts2',
            field=models.CharField(max_length=10, verbose_name='\u0432\u0442\u043e\u0440\u043e\u0439 \u041c\u0422\u0421', blank=True),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='phone_velcom',
            field=models.CharField(max_length=20, verbose_name='Velcom', blank=True),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='phone_velcom2',
            field=models.CharField(max_length=20, verbose_name='\u0432\u0442\u043e\u0440\u043e\u0439 Velcom', blank=True),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='saturday',
            field=models.CharField(default=b'wd', max_length=2, verbose_name='\u0421\u0443\u0431\u0431\u043e\u0442\u0430', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')]),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='site_url',
            field=models.URLField(verbose_name='\u0421\u0430\u0439\u0442', blank=True),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='sunday',
            field=models.CharField(default=b'wd', max_length=2, verbose_name='\u0412\u043e\u0441\u043a\u0440\u0435\u0441\u0435\u043d\u044c\u0435', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')]),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='teaser',
            field=models.TextField(verbose_name='\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='thursday',
            field=models.CharField(default=b'wd', max_length=2, verbose_name='\u0427\u0435\u0442\u0432\u0435\u0440\u0433', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')]),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='title',
            field=models.CharField(max_length=200, verbose_name='title \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b', blank=True),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='tuesday',
            field=models.CharField(default=b'wd', max_length=2, verbose_name='\u0412\u0442\u043e\u0440\u043d\u0438\u043a', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')]),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='wednesday',
            field=models.CharField(default=b'wd', max_length=2, verbose_name='\u0421\u0440\u0435\u0434\u0430', blank=True, choices=[(b'wd', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0434\u0435\u043d\u044c'), (b'sd', '\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c'), (b'hd', '\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439')]),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='work_end',
            field=models.TimeField(null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u0440\u0430\u0431\u043e\u0442\u044b', blank=True),
        ),
        migrations.AddField(
            model_name='tireservice',
            name='work_start',
            field=models.TimeField(null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0440\u0430\u0431\u043e\u0442\u044b', blank=True),
        ),
    ]

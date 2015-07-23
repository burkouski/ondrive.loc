# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='activation_key',
            field=models.CharField(max_length=40, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(upload_to=b'', verbose_name='\u0410\u0432\u0430\u0442\u0430\u0440', blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='nickname',
            field=models.CharField(max_length=100, verbose_name='\u0418\u043c\u044f \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u044e\u0449\u0435\u0435\u0441\u044f \u043d\u0430 \u0441\u0430\u0439\u0442\u0435', blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='sur_name',
            field=models.CharField(max_length=100, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f', blank=True),
        ),
    ]

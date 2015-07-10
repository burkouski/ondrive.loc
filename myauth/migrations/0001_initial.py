# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.auth.models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('sur_name', models.CharField(max_length=100, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f', blank=True)),
                ('avatar', models.ImageField(upload_to=b'', verbose_name='\u0410\u0432\u0430\u0442\u0430\u0440', blank=True)),
                ('nickname', models.CharField(max_length=100, verbose_name='\u0418\u043c\u044f \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u044e\u0449\u0435\u0435\u0441\u044f \u043d\u0430 \u0441\u0430\u0439\u0442\u0435', blank=True)),
                ('activation_key', models.CharField(max_length=40, blank=True)),
                ('key_expires', models.DateTimeField(default=datetime.date.today)),
            ],
            options={
                'verbose_name_plural': '\u041f\u0440\u043e\u0444\u0438\u043b \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]

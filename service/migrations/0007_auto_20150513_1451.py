# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_auto_20150513_1103'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='specializationwork',
            options={'verbose_name': '', 'verbose_name_plural': '\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0437\u0438\u0440\u0443\u044e\u0442\u0441\u044f \u043d\u0430 \u043c\u0430\u0440\u043a\u0430\u0445'},
        ),
        migrations.AddField(
            model_name='specializationwork',
            name='logo',
            field=models.ImageField(upload_to=b'', verbose_name=b'\xd0\x9b\xd0\xbe\xd0\xb3\xd0\xbe\xd1\x82\xd0\xb8\xd0\xbf \xd0\xbc\xd0\xb0\xd1\x80\xd0\xba\xd0\xb8', blank=True),
        ),
    ]

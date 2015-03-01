# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('author', models.CharField(max_length=200, verbose_name='Автор')),
                ('pub_date', models.DateField(verbose_name='Дата публикации')),
                ('review', models.TextField(verbose_name='Отзыв')),
                ('rate', models.PositiveIntegerField(verbose_name='Рейтинг')),
                ('is_moderate', models.BooleanField(verbose_name='Прошел модерацию?', default=None)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

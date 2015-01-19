# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=200, verbose_name='Категория')),
                ('alias', models.SlugField(max_length=100, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок статьи')),
                ('alias', models.SlugField(max_length=100, blank=True)),
                ('pub_date', models.DateField(verbose_name='Дата публикации')),
                ('preview_img', models.ImageField(upload_to='', verbose_name='Превью изображение')),
                ('preview', models.TextField(verbose_name='Вступительный текст')),
                ('text', ckeditor.fields.RichTextField(verbose_name='Полный текст')),
                ('views', models.IntegerField(verbose_name='Количество просмотров')),
                ('category', models.ForeignKey(to='news.Category')),
            ],
            options={
                'ordering': ['-pub_date'],
            },
            bases=(models.Model,),
        ),
    ]

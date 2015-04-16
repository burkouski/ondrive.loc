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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200, verbose_name='Категория')),
                ('alias', models.SlugField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True, verbose_name='Описание категории')),
                ('title', models.CharField(blank=True, max_length=200, verbose_name='title страницы')),
                ('meta_keywords', models.TextField(blank=True, verbose_name='Keywords')),
                ('meta_description', models.TextField(blank=True, verbose_name='Description')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Заголовок статьи')),
                ('alias', models.SlugField(blank=True, max_length=100)),
                ('pub_date', models.DateField(verbose_name='Дата публикации')),
                ('preview_img', models.ImageField(upload_to='', verbose_name='Превью изображение')),
                ('preview', models.TextField(verbose_name='Вступительный текст')),
                ('text', ckeditor.fields.RichTextField(verbose_name='Полный текст')),
                ('views', models.IntegerField(verbose_name='Количество просмотров')),
                ('title', models.CharField(blank=True, max_length=200, verbose_name='title страницы')),
                ('meta_keywords', models.TextField(blank=True, verbose_name='Keywords')),
                ('meta_description', models.TextField(blank=True, verbose_name='Description')),
                ('category', models.ForeignKey(to='news.Category')),
            ],
            options={
                'ordering': ['-pub_date'],
            },
            bases=(models.Model,),
        ),
    ]

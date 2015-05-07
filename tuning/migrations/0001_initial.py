# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Заголовок статьи')),
                ('alias', models.SlugField(blank=True, max_length=100)),
                ('pub_date', models.DateField(verbose_name='Дата публикации')),
                ('preview_img', models.ImageField(verbose_name='Превью изображение', upload_to='')),
                ('preview', models.TextField(verbose_name='Вступительный текст')),
                ('text', ckeditor.fields.RichTextField(verbose_name='Полный текст')),
                ('video', models.CharField(max_length=1000, verbose_name='Ссылка на видео')),
                ('views', models.IntegerField(verbose_name='Количество просмотров')),
                ('title', models.CharField(blank=True, max_length=200, verbose_name='title страницы')),
                ('meta_keywords', models.TextField(blank=True, verbose_name='Keywords')),
                ('meta_description', models.TextField(blank=True, verbose_name='Description')),
            ],
            options={
                'ordering': ['-pub_date'],
            },
            bases=(models.Model,),
        ),
    ]

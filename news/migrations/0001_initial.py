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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('category', models.CharField(verbose_name='Категория', max_length=200)),
                ('alias', models.SlugField(max_length=100, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(verbose_name='Заголовок статьи', max_length=200)),
                ('alias', models.SlugField(max_length=100, blank=True)),
                ('pub_date', models.DateField(verbose_name='Дата публикации')),
                ('preview_img', models.ImageField(verbose_name='Превью изображение', upload_to='')),
                ('preview', models.TextField(verbose_name='Вступительный текст')),
                ('text', ckeditor.fields.RichTextField(verbose_name='Полный текст')),
                ('category', models.ForeignKey(to='news.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

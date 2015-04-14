# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(verbose_name='Заголовок страницы', max_length=200)),
                ('alias', models.SlugField(blank=True, max_length=100)),
                ('text', ckeditor.fields.RichTextField(verbose_name='Текст страницы')),
                ('title', models.CharField(blank=True, verbose_name='title страницы', max_length=200)),
                ('meta_keywords', models.TextField(blank=True, verbose_name='Keywords')),
                ('meta_description', models.TextField(blank=True, verbose_name='Description')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

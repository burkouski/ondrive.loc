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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=200, verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f')),
                ('alias', models.SlugField(max_length=100, blank=True)),
                ('description', models.TextField(verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xba\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd0\xb8', blank=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'title \xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x86\xd1\x8b', blank=True)),
                ('meta_keywords', models.TextField(verbose_name=b'meta keywords', blank=True)),
                ('meta_description', models.TextField(verbose_name=b'meta description', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'\xd0\x97\xd0\xb0\xd0\xb3\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xba \xd1\x81\xd1\x82\xd0\xb0\xd1\x82\xd1\x8c\xd0\xb8')),
                ('alias', models.SlugField(max_length=100, blank=True)),
                ('pub_date', models.DateField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbf\xd1\x83\xd0\xb1\xd0\xbb\xd0\xb8\xd0\xba\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8')),
                ('preview_img', models.ImageField(upload_to=b'', verbose_name=b'\xd0\x9f\xd1\x80\xd0\xb5\xd0\xb2\xd1\x8c\xd1\x8e \xd0\xb8\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('preview', models.TextField(verbose_name=b'\xd0\x92\xd1\x81\xd1\x82\xd1\x83\xd0\xbf\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x8b\xd0\xb9 \xd1\x82\xd0\xb5\xd0\xba\xd1\x81\xd1\x82')),
                ('text', ckeditor.fields.RichTextField(verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb\xd0\xbd\xd1\x8b\xd0\xb9 \xd1\x82\xd0\xb5\xd0\xba\xd1\x81\xd1\x82')),
                ('video', models.CharField(max_length=1000, null=True, verbose_name=b'\xd0\xa1\xd1\x81\xd1\x8b\xd0\xbb\xd0\xba\xd0\xb0 \xd0\xbd\xd0\xb0 \xd0\xb2\xd0\xb8\xd0\xb4\xd0\xb5\xd0\xbe', blank=True)),
                ('views', models.IntegerField(verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbb\xd0\xb8\xd1\x87\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe \xd0\xbf\xd1\x80\xd0\xbe\xd1\x81\xd0\xbc\xd0\xbe\xd1\x82\xd1\x80\xd0\xbe\xd0\xb2')),
                ('title', models.CharField(max_length=200, verbose_name=b'title \xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x86\xd1\x8b', blank=True)),
                ('meta_keywords', models.TextField(verbose_name=b'Keywords', blank=True)),
                ('meta_description', models.TextField(verbose_name=b'Description', blank=True)),
                ('change_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(to='news.Category')),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
    ]

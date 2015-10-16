# -*- coding: utf-8 -*-
from django.db import models
from pytils import translit
from ckeditor.fields import RichTextField
from django.core.urlresolvers import reverse
import datetime


class Category(models.Model):
    category = models.CharField(u'Категория', max_length=200)
    alias = models.SlugField(max_length=100, blank=True)
    description = models.TextField(u'Описание категории', blank=True)
    title = models.CharField(u'title страницы', max_length=200, blank=True)
    meta_keywords = models.TextField(u'meta keywords', blank=True)
    meta_description = models.TextField(u'meta description', blank=True)
    lastmod = models.DateTimeField(auto_now=True, blank=True, null=True)


    def __unicode__(self):
        return self.category

    def save(self, *args, **kwargs):
        if not self.title:
            self.title = self.category
        if not self.alias:
            self.alias = translit.slugify(self.category)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(u'news:category_post_list', kwargs={u'category_alias': self.alias})


class Post(models.Model):
    name = models.CharField(u'Заголовок статьи', max_length=200)
    alias = models.SlugField(max_length=100, blank=True)
    pub_date = models.DateField(u'Дата публикации')
    preview_img = models.ImageField(u'Превью изображение')
    preview = models.TextField(u'Вступительный текст')
    text = RichTextField(u'Полный текст')
    video = models.CharField(u'Ссылка на видео', max_length=1000, null=True, blank=True)
    category = models.ForeignKey(Category)
    views = models.IntegerField(u'Количество просмотров')
    title = models.CharField(u'title страницы', max_length=200, blank=True)
    meta_keywords = models.TextField(u'Keywords', blank=True)
    meta_description = models.TextField(u'Description', blank=True)
    lastmod = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        ordering = [u'-pub_date']

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.title:
            self.title = self.name
        if not self.alias:
            self.alias = translit.slugify(self.name)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(u'news:post_detail', kwargs={u'post_alias': self.alias, u'category_alias': self.category.alias})



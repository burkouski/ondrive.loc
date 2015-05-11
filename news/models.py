# -*- coding: utf-8 -*-
from django.db import models
from pytils import translit
from ckeditor.fields import RichTextField
from django.core.urlresolvers import reverse


class Category(models.Model):
    category = models.CharField('Категория', max_length=200)
    alias = models.SlugField(max_length=100, blank=True)
    description = models.TextField('Описание категории', blank=True)
    title = models.CharField('title страницы', max_length=200, blank=True)
    meta_keywords = models.TextField('meta keywords', blank=True)
    meta_description = models.TextField('meta description', blank=True)
    def __unicode__(self):
        return self.category

    def save(self, *args, **kwargs):
        if not self.title:
            self.title = self.category
        if not self.alias:
            self.alias = translit.slugify(self.category)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('news:category_post_list', kwargs={'category_alias': self.alias})


class Post(models.Model):
    name = models.CharField('Заголовок статьи', max_length=200)
    alias = models.SlugField(max_length=100, blank=True)
    pub_date = models.DateField('Дата публикации')
    preview_img = models.ImageField('Превью изображение')
    preview = models.TextField('Вступительный текст')
    text = RichTextField('Полный текст')
    video = models.CharField('Ссылка на видео', max_length=1000, null=True, blank=True)
    category = models.ForeignKey(Category)
    views = models.IntegerField('Количество просмотров')
    title = models.CharField('title страницы', max_length=200, blank=True)
    meta_keywords = models.TextField('Keywords', blank=True)
    meta_description = models.TextField('Description', blank=True)

    class Meta:
        ordering = ['-pub_date']

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.title:
            self.title = self.name
        if not self.alias:
            self.alias = translit.slugify(self.name)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('news:post_detail', kwargs={'post_alias': self.alias, 'category_alias': self.category.alias})



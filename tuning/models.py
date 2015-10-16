# -*- coding: utf-8 -*-
from django.db import models
from pytils import translit
from ckeditor.fields import RichTextField
from django.core.urlresolvers import reverse


class Post(models.Model):
    name = models.CharField(u'Заголовок статьи', max_length=200)
    alias = models.SlugField(max_length=100, blank=True)
    pub_date = models.DateField(u'Дата публикации')
    preview_img = models.ImageField(u'Превью изображение')
    preview = models.TextField(u'Вступительный текст')
    text = RichTextField(u'Полный текст')
    video = models.CharField(u'Ссылка на видео', max_length=1000, blank=True)
    views = models.IntegerField(u'Количество просмотров')
    title = models.CharField(u'title страницы', max_length=200, blank=True)
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
        return reverse('tuning:tuning_post_detail', kwargs={'post_alias': self.alias})

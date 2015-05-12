# -*- coding: utf-8 -*-
from django.db import models
from pytils import translit
from ckeditor.fields import RichTextField
from django.core.urlresolvers import reverse

class Page(models.Model):
    name = models.CharField('Заголовок страницы', max_length=200)
    alias = models.SlugField(max_length=100, blank=True)
    text = RichTextField('Текст страницы')
    title = models.CharField('title страницы', max_length=200, blank=True)
    meta_keywords = models.TextField('Keywords', blank=True)
    meta_description = models.TextField('Description', blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.title:
            self.title = self.name
        if not self.alias:
            self.alias = translit.slugify(self.name)
        super(Page, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('page_view', kwargs={'page_alias': self.alias})

# -*- coding: utf-8 -*-
from django.db import models
from pytils import translit
from ckeditor.fields import RichTextField
from django.core.urlresolvers import reverse

class Page(models.Model):
    name = models.CharField(u'Заголовок страницы', max_length=200)
    alias = models.SlugField(max_length=100, blank=True)
    text = RichTextField(u'Текст страницы')
    title = models.CharField(u'title страницы', max_length=200, blank=True)
    meta_keywords = models.TextField(u'Keywords', blank=True)
    meta_description = models.TextField(u'Description', blank=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.title:
            self.title = self.name
        if not self.alias:
            self.alias = translit.slugify(self.name)
        super(Page, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(u'page_view', kwargs={u'page_alias': self.alias})

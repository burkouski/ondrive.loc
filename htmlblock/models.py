# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField


class Htmlblock(models.Model):
    ALIGN_CHOICES = (
        ('text-left', u'Слева'),
        ('text-right', u'Справа'),
        ('text-center', u'По центру'),
    )
    label = models.CharField(u'На звание для индентификации', max_length=200)
    name = models.CharField(u'Заголовок блока', max_length=200)
    name_align = models.CharField(max_length=100, choices=ALIGN_CHOICES)
    text = RichTextField(u'Текст блока')
    text_align = models.CharField(max_length=100, choices=ALIGN_CHOICES)

    def __unicode__(self):
        return self.label
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


# Create your models here.
class Review(models.Model):
    author = models.CharField(u'Автор', max_length=200)
    pub_date = models.DateField(u'Дата публикации', auto_now_add=True)
    review = models.TextField(u'Отзыв')
    rate = models.PositiveIntegerField(u'Рейтинг')
    is_moderate = models.NullBooleanField(u"Прошел модерацию?", default=None)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(u'content_type', u'object_id')

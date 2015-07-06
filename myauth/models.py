# -*- coding: utf-8 -*-
import datetime
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(u'Имя',max_length=100, blank=True)
    sur_name = models.CharField(u'Фамилия',max_length=100, blank=True)
    avatar = models.ImageField(u'Аватар', blank=True)
    nickname = models.CharField(u'Имя отображающееся на сайте',max_length=100, blank=True)
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(default=datetime.date.today)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural=u'Профил пользователя'

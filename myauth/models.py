# -*- coding: utf-8 -*-
import datetime
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class UserProfile(User):
    user = models.OneToOneField(User)
    sur_name = models.CharField(u'Фамилия',max_length=100, blank=True)
    avatar = models.ImageField(u'Аватар', blank=True)
    nickname = models.CharField(u'Имя отображающееся на сайте',max_length=100, blank=True)
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(default=datetime.date.today)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural=u'Профил пользователя'

    def save(self, *args, **kwargs):
        # Сначала - обычное сохранение
        super(UserProfile, self).save(*args, **kwargs)

        # Проверяем, указан ли логотип
        if self.avatar:
            _MAX_SIZE = 300
            filepath = self.avatar.path
            width = self.avatar.width
            height = self.avatar.height

            max_size = max(width, height)

            # Может, и не надо ничего менять?
            if max_size > _MAX_SIZE:
                # Надо, Федя, надо
                image = Image.open(filepath)
                ratio = max_size/_MAX_SIZE
                # resize - безопасная функция, она создаёт новый объект, а не
                # вносит изменения в исходный, поэтому так

                print(_MAX_SIZE, ratio)
                print(width/ratio)
                image = image.resize(
                    (int(width/ratio), int(height/ratio)  # Сохраняем пропорции
                ),
                    Image.ANTIALIAS
                )
                # И не забыть сохраниться
                image.save(filepath)

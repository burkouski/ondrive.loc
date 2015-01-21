# -*- coding: utf-8 -*-
import urllib
import re
from pytils import translit
from django.db import models
from django.core.urlresolvers import reverse

from ckeditor.fields import RichTextField
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
import json


# Абстрактная модель для сервисов
class Service(models.Model):
    name = models.CharField("Название сервиса", max_length=200)
    alias = models.SlugField(max_length=100, blank=True)
    teaser = models.TextField('Краткое описание')
    address = models.CharField('Адрес', max_length=200)
    phone_velcom = models.CharField("Velcom", max_length=10, blank=True)
    phone_mts = models.CharField("МТС", max_length=10, blank=True)
    phone_life = models.CharField("Life", max_length=10, blank=True)
    phone_city = models.CharField("Городской", max_length=10, blank=True)
    work_start = models.TimeField('Время начала работы')
    work_end = models.TimeField('Время завершения работы')
    break_time_start = models.TimeField('Время начала обеда', blank=True)
    break_time_end = models.TimeField('Время завершения обеда', blank=True)
    holiday = models.CharField("Сокращенные дни", max_length=10, blank=True)
    holiday_time_start = models.TimeField('Время начала сокращенного дня', blank=True)
    holiday_time_end = models.TimeField('Время завершения сокращенного дня', blank=True)
    monday = models.BooleanField('Понедельник', blank=True)
    tuesday = models.BooleanField('Вторник', blank=True)
    wednesday = models.BooleanField('Среда', blank=True)
    thursday = models.BooleanField('Четверг', blank=True)
    friday = models.BooleanField('Пятница', blank=True)
    saturday = models.BooleanField('Суббота', blank=True)
    sunday = models.BooleanField('Воскресенье', blank=True)
    email = models.EmailField("Email", blank=True)
    site_url = models.URLField('Сайт', blank=True)
    full_desc = RichTextField("Полное описание", blank=True)
    logo = models.ImageField("Логотип компании", blank=True)
    is_top = models.BooleanField("Выводить в топ на главной?", default=None)
    latitude = models.CharField('Широта', max_length=200, blank=True)
    longitude = models.CharField('Долгота', max_length=200, blank=True)
    title = models.CharField('title страницы', max_length=200, blank=True)
    meta_keywords = models.TextField('Keywords', blank=True)
    meta_description = models.TextField('Description', blank=True)

    class Meta:
        abstract = True

    # Получаем рабочие дни ввиде списка Используеть в tastypie api
    def get_workdays_list(self):
        workDaysList = [self.monday, self.tuesday, self.wednesday, self.thursday, self.friday, self.saturday,
                        self.sunday]
        return workDaysList

    def get_logo_img(self):
        return u'<img src="%s" />' % self.logo.url

    def save(self):
        address = re.sub(' +', '+', self.address)
        location = "%s" % address
        location = location.encode('utf-8')

        if self.pk is not None:
            origin_address = Service(pk=self.pk)

        if not self.latitude or not self.longitude or (origin_address.address != self.address):
            latlng = self.geocode(location)
            latlng = latlng.split(' ')
            self.latitude = latlng[0]
            self.longitude = latlng[1]

        # Если не задано поле alias Получаем его из поля name
        if not self.alias:
            self.alias = translit.slugify(self.name)

        # Если не задано поле title Получаем его из поля name
        if not self.title:
            self.title = self.name

        if not self.logo:
            self.logo = '/static/img/nophoto.png'

        super(Service, self).save()

    # Преобразуем поле address в координаты для полей latitude и longitude
    def geocode(self, location):
        format = "json"
        location = urllib.parse.quote_plus(location)
        request = "http://geocode-maps.yandex.ru/1.x/?&geocode=%s&format=%s" % (location, format)
        data = urllib.request.urlopen(request).read()
        data = json.loads(data.decode())
        return data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]

    def __str__(self):
        return self.name


class AutoService(Service):
    def get_absolute_url(self):
        return reverse('service:autoservice_detail', kwargs={'service_alias': self.alias})

    class Meta:
        verbose_name = u"Автосервис"
        verbose_name_plural = u"Автосервисы"


class TireService(Service):
    pass

    class Meta:
        verbose_name = u"Шиномонтаж"
        verbose_name_plural = u"Шиномонтажи"


class CarWash(Service):
    pass

    class Meta:
        verbose_name = u"Автомойка"
        verbose_name_plural = u"Автомойки"


class AutoServiceWork(models.Model):
    autoservice = models.OneToOneField(AutoService, related_name="autoservice")

    # АВТОЭЛЕКТРИКА
    comp_diag = models.BooleanField(verbose_name='Компьютерная диагностика')
    rep_elect = models.BooleanField('Ремонт электрооборудования')
    rep_gen = models.BooleanField('Ремонт генераторов, стартеров')

    # КУЗОВНОЙ РЕМОНТ
    car_paint = models.BooleanField('Покраска авто')
    rec_geo = models.BooleanField('Восстановление геометрии')
    body_work = models.BooleanField('Кузовные работы, рихтовка')
    welding = models.BooleanField('Сварочные работы')
    select_paint = models.BooleanField('Подбор краски')
    rep_bump = models.BooleanField('Ремонт бамперов, пластика')
    rep_paint = models.BooleanField('Беспокрасочное удаление вмятин')
    sand_blasting = models.BooleanField('Пескоструйная обработка')
    cor_treatment = models.BooleanField('Антикоррозийная обработка')

    class Meta:
        verbose_name = u""
        verbose_name_plural = u"Виды работ"

    def get_work_dict(self):
        electrician_list = ['comp_diag', 'rep_elect', 'rep_gen']
        work_dict = {'Автоэлектрика': self.get_list(electrician_list),
                     'Кузовной ремонт': [
            [self._meta.get_field("car_paint").verbose_name, self.car_paint],
            [self._meta.get_field("rec_geo").verbose_name, self.rec_geo],
            [self._meta.get_field("body_work").verbose_name, self.body_work],
            [self._meta.get_field("welding").verbose_name, self.welding],
            [self._meta.get_field("select_paint").verbose_name, self.select_paint],
            [self._meta.get_field("rep_bump").verbose_name, self.rep_bump],
            [self._meta.get_field("rep_paint").verbose_name, self.rep_paint],
            [self._meta.get_field("sand_blasting").verbose_name, self.sand_blasting],
            [self._meta.get_field("cor_treatment").verbose_name, self.cor_treatment]
                    ]
        }
        return work_dict

    def get_list(self, f_list):
        f_list = [[self._meta.get_field(field).verbose_name, self.__dict__[field]] for field in f_list if self.__dict__[field]]
        return f_list

class TireServiceWork(models.Model):
    pass


class CarWashWork(models.Model):
    pass
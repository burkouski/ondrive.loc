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
    work_start = models.TimeField('Время начала работы', null=True)
    work_end = models.TimeField('Время завершения работы', null=True)
    break_time_start = models.TimeField('Время начала обеда', null=True)
    break_time_end = models.TimeField('Время завершения обеда', null=True)
    holiday = models.CharField("Сокращенные дни", max_length=10, blank=True)
    holiday_time_start = models.TimeField('Время начала сокращенного дня', null=True)
    holiday_time_end = models.TimeField('Время завершения сокращенного дня', null=True)
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


class AutoserviceWork(models.Model):
    work_name = models.CharField("Вид работы", max_length=200)

    class Meta:
        abstract = True

    def __str__(self):
        return self.work_name

    def get_model_name(self):
        model_name = self._meta.verbose_name_plural.title()
        return model_name
        # def get_work_dict(self):
        #     work_dict = {}
        #     field_list = self._meta.get_all_field_names()[1:]
        #     model_name = self._meta.verbose_name_plural
        #     work_dict ={'fgfgf' :[[self._meta.get_field(field).verbose_name, self.__dict__[field]] for field in field_list if self.__dict__[field]]}
        #     return work_dict


        # АВТОЭЛЕКТРИКА


class ElectricianWork(AutoserviceWork):
    class Meta:
        verbose_name = u""
        verbose_name_plural = u"Автоэлектрика"


# КУЗОВНОЙ РЕМОНТ
class BodyRepairWork(AutoserviceWork):
    class Meta:
        verbose_name = u""
        verbose_name_plural = u"Кузовной ремонт"


#РЕМОНТ ДВИГАТЕЛЯ
class EngineRepairWork(AutoserviceWork):
    class Meta:
        verbose_name = u""
        verbose_name_plural = u"Ремонт двигателя"


#Ремонт топливной системы
class FuelSystemRepairWork(AutoserviceWork):

    class Meta:
        verbose_name = u""
        verbose_name_plural = u"Ремонт топливной системы"


#Ремонт подвески, трансмиссии
class SuspensionRepairWork(AutoserviceWork):

    class Meta:
        verbose_name = u""
        verbose_name_plural = u"Ремонт подвески"


#Тормозная система
class BreakSystemRepairWork(AutoserviceWork):
    autoservice = models.ManyToManyField(AutoService, related_name='break_system_repair_work')

    class Meta:
        verbose_name = u""
        verbose_name_plural = u"Тормозная система"


#Диагностика автомобилей
class AutoDiagWork(AutoserviceWork):
    autoservice = models.ManyToManyField(AutoService, related_name='auto_diag_work')

    class Meta:
        verbose_name = u""
        verbose_name_plural = u"Диагностика автомобилей"


#Ремонт КПП
class KppRepairWork(AutoserviceWork):
    autoservice = models.ManyToManyField(AutoService, related_name='kpp_repair_work')

    class Meta:
        verbose_name = u""
        verbose_name_plural = u"Ремонт КПП"


#Кондиционер, радиаторы
class AirConditionRepairWork(AutoserviceWork):
    autoservice = models.ManyToManyField(AutoService, related_name='air_condition_repair_work')

    class Meta:
        verbose_name = u""
        verbose_name_plural = u"Кондиционер, радиаторы"


#Автостекла
class AutoglassesRepairWork(AutoserviceWork):
    autoservice = models.ManyToManyField(AutoService, related_name='autoglasses_repair_work')

    class Meta:
        verbose_name = u""
        verbose_name_plural = u"Автостекла"


#Газовое оборудование
class GasAppliancesRepairWork(AutoserviceWork):
    autoservice = models.ManyToManyField(AutoService, related_name='gas_appliances_repair_work')

    class Meta:
        verbose_name = u""
        verbose_name_plural = u"Газовое оборудование"


#Замена масла, ремней
class OilReplaceWork(AutoserviceWork):
    autoservice = models.ManyToManyField(AutoService, related_name='oil_replace_work')

    class Meta:
        verbose_name = u""
        verbose_name_plural = u"Замена масла"


#Аудио, Сигнализации
class AudioAlarmRepairWork(AutoserviceWork):
    autoservice = models.ManyToManyField(AutoService, related_name='audio_alarm_repair_work')

    class Meta:
        verbose_name = u""
        verbose_name_plural = u"Аудио, Сигнализации"


#Тюнинг
class TuningWork(AutoserviceWork):
    autoservice = models.ManyToManyField(AutoService, related_name='tuning_work')

    class Meta:
        verbose_name = u""
        verbose_name_plural = u"Тюнинг"


#Прочее
class OtherAutogWork(AutoserviceWork):
    autoservice = models.ManyToManyField(AutoService, related_name='other_auto_work')

    class Meta:
        verbose_name = u""
        verbose_name_plural = u"Прочее"



# class TireServiceWork(models.Model):
#     pass
#
#
# class CarWashWork(models.Model):
#     pass


class AutoService(Service):
    # Виды работ
    electrician_work = models.ManyToManyField(ElectricianWork, related_name='electrician_work',
                                              verbose_name='Автоэлектрика')
    body_repair_work = models.ManyToManyField(BodyRepairWork, related_name='body_repair_work',
                                              verbose_name='Кузовной ремонт')
    engine_repair_work = models.ManyToManyField(EngineRepairWork, related_name='body_repair_work',
                                                verbose_name='Ремонт двигателя')
    fuel_system_repair_work = models.ManyToManyField(FuelSystemRepairWork, related_name='fuel_system_repair_work')
    suspension_repair_work = models.ManyToManyField(SuspensionRepairWork, related_name='suspension_repair_work')

    class Meta:
        verbose_name = u"Автосервис"
        verbose_name_plural = u"Автосервисы"

    def get_absolute_url(self):
        return reverse('service:autoservice_detail', kwargs={'service_alias': self.alias})

    def get_work_list(self):
        work_list = []
        model_list = [ElectricianWork.objects.filter(electrician_work=self.id),
                      BodyRepairWork.objects.filter(body_repair_work=self.id)
        ]
        for model in model_list:
            for obj in model:
                work_list.append(obj)

        return work_list


# class TireService(Service):
#     pass
#
#     class Meta:
#         verbose_name = u"Шиномонтаж"
#         verbose_name_plural = u"Шиномонтажи"
#
#
# class CarWash(Service):
#     pass
#
#     class Meta:
#         verbose_name = u"Автомойка"
#         verbose_name_plural = u"Автомойки"


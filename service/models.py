# -*- coding: utf-8 -*-
import urllib
import re
from pytils import translit
from django.db import models
from django.core.urlresolvers import reverse
from ckeditor.fields import RichTextField
from reviews.models import Review
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
import json
from django.db.models import Avg


# Абстрактная модель для сервисов
class Service(models.Model):
    name = models.CharField("Название сервиса", max_length=200)
    alias = models.SlugField(max_length=100, blank=True)
    teaser = models.TextField('Краткое описание')
    address = models.CharField('Адрес', max_length=200)
    phone_velcom = models.CharField("Velcom", max_length=20, blank=True)
    phone_velcom2 = models.CharField("второй Velcom", max_length=20, blank=True)
    phone_mts = models.CharField("МТС", max_length=20, blank=True)
    phone_mts2 = models.CharField("второй МТС", max_length=10, blank=True)
    phone_life = models.CharField("Life", max_length=20, blank=True)
    phone_life2 = models.CharField("второй Life", max_length=20, blank=True)
    phone_city = models.CharField("Городской", max_length=20, blank=True)
    phone_city2 = models.CharField("второй Городской", max_length=20, blank=True)
    work_start = models.TimeField('Время начала работы', null=True, blank=True)
    work_end = models.TimeField('Время завершения работы', null=True, blank=True)
    break_time_start = models.TimeField('Время начала обеда', null=True, blank=True)
    break_time_end = models.TimeField('Время завершения обеда', null=True, blank=True)
    holiday = models.CharField("Сокращенные дни", max_length=10, blank=True)
    holiday_time_start = models.TimeField('Время начала сокращенного дня', null=True, blank=True)
    holiday_time_end = models.TimeField('Время завершения сокращенного дня', null=True, blank=True)
    monday = models.BooleanField('Понедельник',default=None, blank=True)
    tuesday = models.BooleanField('Вторник',default=None, blank=True)
    wednesday = models.BooleanField('Среда',default=None, blank=True)
    thursday = models.BooleanField('Четверг',default=None, blank=True)
    friday = models.BooleanField('Пятница',default=None, blank=True)
    saturday = models.BooleanField('Суббота',default=None, blank=True)
    sunday = models.BooleanField('Воскресенье',default=None, blank=True)
    email = models.EmailField("Email", blank=True)
    site_url = models.URLField('Сайт', blank=True)
    full_desc = RichTextField("Полное описание", blank=True)
    logo = models.ImageField("Логотип компании", blank=True)
    is_top = models.BooleanField("Выводить в топ на главной?", default=None, blank=True)
    latitude = models.CharField('Широта', max_length=200, blank=True)
    longitude = models.CharField('Долгота', max_length=200, blank=True)
    title = models.CharField('title страницы', max_length=200, blank=True)
    meta_keywords = models.TextField('Keywords', blank=True)
    meta_description = models.TextField('Description', blank=True)

    class Meta:
        abstract = True

    # Получаем рабочие дни ввиде списка Используеть в tastypie api
    def get_workday_list(self):
        work_day_list = [[self.monday, 'пн'], [self.tuesday, 'вт'], [self.wednesday, 'ср'], [self.thursday, 'чт'], [self.friday, 'пт'], [self.saturday, 'сб'],
                        [self.sunday, 'вс']]
        return work_day_list

    def get_logo_img(self):
        return u'<img src="%s" />' % self.logo.url

    def get_rating(self):
        rating = self.reviews.filter(is_moderate=True).aggregate(Avg('rate'))['rate__avg']
        return rating

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

    def get_content_type(self):
        return ContentType.objects.get_for_model(self).id

    # Преобразуем поле address в координаты для полей latitude и longitude
    def geocode(self, location):
        format = "json"
        # для python 3
        #location = urllib.parse.quote_plus(location)
        location = urllib.quote_plus(location)
        request = "http://geocode-maps.yandex.ru/1.x/?&geocode=%s&format=%s" % (location, format)
        # для python 3
        #data = urllib.request.urlopen(request).read()
        data = urllib.urlopen(request).read()
        # для python 3
        # data = json.loads(data.decode())
        data = json.loads(data)
        return data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]

    def __unicode__(self):
        return self.name


class Work(models.Model):
    work_name = models.CharField("Вид работы", max_length=200)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.work_name

    def get_model_name(self):
        model_name = self._meta.verbose_name_plural.title()
        return model_name


class AddServices(Work):
    work_field_name = 'add_services'

    class Meta:
        verbose_name = u""
        verbose_name_plural = u"Дополнительные услуги"

#################### АВТОСЕРВИСЫ ####################

# специализация авто
class SpecializationWork(Work):
    work_field_name = 'specialization_work'
    logo = models.ImageField("Логотип марки", blank=True)
    class Meta:
        verbose_name = u""
        verbose_name_plural = u"Специализируются на марках"


class AutoserviceWork(Work):
    work_field_name = 'autoservice_work'

    class Meta:
        verbose_name = u""
        verbose_name_plural = u"Виды работ"



class AutoService(Service):
    # Виды работ
    specialization_work = models.ManyToManyField(SpecializationWork, related_name='specialization_work',
                                              verbose_name='Специализирующиеся на марке', blank=True)
    autoservice_work = models.ManyToManyField(AutoserviceWork, related_name='autoservice_work',
                                              verbose_name='Виды работ', blank=True)
    add_services = models.ManyToManyField(AddServices, related_name='autoservice_add_services',
                                                     verbose_name='Дополнительные услуги', blank=True)

    reviews = GenericRelation(Review)

    class Meta:
        verbose_name = u"Автосервис"
        verbose_name_plural = u"Автосервисы"

    def get_absolute_url(self):
        return reverse('service:autoservice_detail', kwargs={'service_alias': self.alias})



# class TireService(Service):
#     pass
#
#     class Meta:
#         verbose_name = u"Шиномонтаж"
#         verbose_name_plural = u"Шиномонтажи"
#

#################### АВТОМОЙКИ ####################
class TypeCarWash(Work):
    work_field_name = 'type_carwash'

    class Meta:
        verbose_name = u""
        verbose_name_plural = u"Вид мойки"


class TypeVehicle(Work):
    work_field_name = 'type_vehicle'

    class Meta:
        verbose_name = u""
        verbose_name_plural = u"Вид транспорта"


class CarWashServices(Work):
    work_field_name = 'car_wash_services'

    class Meta:
        verbose_name = u""
        verbose_name_plural = u"Услуги"



class CarWash(Service):
    type_carwash = models.ManyToManyField(TypeCarWash, related_name='type_carwash',
                                              verbose_name='Вид мойки', blank=True)
    type_vehicle = models.ManyToManyField(TypeVehicle, related_name='type_vehicle',
                                              verbose_name='Вид транспорта', blank=True)
    car_wash_services = models.ManyToManyField(CarWashServices, related_name='car_wash_services',
                                                verbose_name='Услуги', blank=True)
    add_services = models.ManyToManyField(AddServices, related_name='carwash_add_services',
                                                     verbose_name='Дополнительные услуги', blank=True)
    reviews = GenericRelation(Review)

    class Meta:
        verbose_name = u"Автомойка"
        verbose_name_plural = u"Автомойки"

    def get_absolute_url(self):
        return reverse('service:carwash_detail', kwargs={'service_alias': self.alias})


#################### ШИНОМОНТАЖИ ####################

class TireWork(Work):
    work_field_name = 'tire_work'

    class Meta:
        verbose_name = u""
        verbose_name_plural = u"Шины"


class DiscWork(Work):
    work_field_name = 'disc_work'

    class Meta:
        verbose_name = u""
        verbose_name_plural = u"Диски"


class TireService(Service):
    tire_work = models.ManyToManyField(TireWork, related_name='tire_work',
                                              verbose_name='Шины', blank=True)
    disc_work = models.ManyToManyField(DiscWork, related_name='disc_work',
                                              verbose_name='Диски', blank=True)
    add_services = models.ManyToManyField(AddServices, related_name='tire_add_services',
                                                     verbose_name='Дополнительные услуги', blank=True)
    reviews = GenericRelation(Review)

    class Meta:
        verbose_name = u"Шиномонтаж"
        verbose_name_plural = u"Шиномонтажи"

    def get_absolute_url(self):
        return reverse('service:tireservice_detail', kwargs={'service_alias': self.alias})
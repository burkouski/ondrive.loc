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
    break_time_start = models.TimeField('Время начала обеда',  null=True)
    break_time_end = models.TimeField('Время завершения обеда',  null=True)
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


class AutoserviceWork(models.Model):

    class Meta:
        abstract = True

    def get_work_dict(self):
        work_dict = {}
        field_list = self._meta.get_all_field_names()[1:]
        model_name = self._meta.verbose_name_plural
        work_dict ={'fgfgf' :[[self._meta.get_field(field).verbose_name, self.__dict__[field]] for field in field_list if self.__dict__[field]]}
        return work_dict


 # АВТОЭЛЕКТРИКА
class ElectricianWork(AutoserviceWork):
    autoservice = models.OneToOneField(AutoService, related_name='electrician_work')
    rep_elect = models.BooleanField('Ремонт электрооборудования')
    rep_control_unit = models.BooleanField('Ремонт блоков управления')
    rep_gen = models.BooleanField('Ремонт генераторов, стартеров')
    inst_ksen = models.BooleanField('Установка ксенона')
    inst_park = models.BooleanField('Установка парктроника')
    rep_range = models.BooleanField('ремонт фар')
    reg_range = models.BooleanField('регулировка света фар')

    class Meta:
        verbose_name = u""
        verbose_name_plural = u"Автоэлектрика"


# КУЗОВНОЙ РЕМОНТ
class BodyRepairWork(AutoserviceWork):
    autoservice = models.OneToOneField(AutoService, related_name='body_repair_work')
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
        verbose_name_plural = u"Кузовной ремонт"


#РЕМОНТ ДВИГАТЕЛЯ
class EngineRepairWork(AutoserviceWork):
    autoservice = models.OneToOneField(AutoService, related_name='engine_repair_work')
    rep_gas_ing = models.BooleanField('Ремонт бензинового двигателя')
    rep_dies_ing = models.BooleanField('Ремонт дизельного двигателя')
    rep_hybr_ing = models.BooleanField('Ремонт двигателей гибридных')
    rep_turb_ing = models.BooleanField('Ремонт турбин')
    rep_gbc = models.BooleanField('Ремонт ГБЦ')
    mot_prot = models.BooleanField('Установка защиты мотора СЗМО')
    rep_cool = models.BooleanField('Ремонт системы охлаждения')
    repl_belt= models.BooleanField('Замена ремней ГРМ')

    class Meta:
        verbose_name = u""
        verbose_name_plural = u"Ремонт двигателя"


#Ремонт топливной системы
class FuelSystemRepairWork(AutoserviceWork):
    autoservice = models.OneToOneField(AutoService, related_name='fuel_system_repair_work')
    rep_gas_sys = models.BooleanField('Ремонт бензиновой топливной системы')
    rep_dies_sys = models.BooleanField('Ремонт дизельной топливной системы')
    rep_fuel_pump = models.BooleanField('Ремонт топливных насосов (ТНВД)')
    flush_fuel_sys = models.BooleanField('Промывка топливной системы')
    select_paint = models.BooleanField('Ультразвуковая чистка форсунок')
    clean_nozz = models.BooleanField('Ремонт инжектора')
    rep_bosch = models.BooleanField('Ремонт BOSCH')
    rep_com_rail = models.BooleanField('Ремонт Common Rail')
    rep_fuel_tanks = models.BooleanField('Ремонт бензобаков')
    rep_turb = models.BooleanField('Ремонт турбин')

    class Meta:
        verbose_name = u""
        verbose_name_plural = u"Ремонт топливной системы"


#Ремонт подвески, трансмиссии
class SuspensionRepairWork(AutoserviceWork):
    autoservice = models.OneToOneField(AutoService, related_name='suspension_repair_work')
    rep_suspen = models.BooleanField('Ремонт подвески')
    collapse_toe = models.BooleanField('Развал схождение')
    rep_rear_beam = models.BooleanField('Ремонт задней балки')
    rep_cardan_shafts = models.BooleanField('Ремонт карданных валов')
    test_absord = models.BooleanField('Шок-тест амортизаторов')

    class Meta:
        verbose_name = u""
        verbose_name_plural = u"Ремонт подвески"


#Тормозная система
class BreakSystemRepairWork(AutoserviceWork):
    autoservice = models.OneToOneField(AutoService, related_name='break_system_repair_work')
    rep_break_sys = models.BooleanField('Ремонт тормозной системы')
    groove_break_disc = models.BooleanField('Проточка тормозных дисков')
    repl_break_disc = models.BooleanField('Замена тормозных колодок и дисков')
    rep_calipers = models.BooleanField('Ремонт суппортов')

    class Meta:
        verbose_name = u""
        verbose_name_plural = u"Тормозная система"


#Диагностика автомобилей
class AutoDiagWork(AutoserviceWork):
    autoservice = models.OneToOneField(AutoService, related_name='auto_diag_work')
    comp_diad = models.BooleanField('Компьютерная диагностика')
    diag_suspen = models.BooleanField('Диагностика подвески')
    diag_ing = models.BooleanField('Диагностика двигателя')
    diag_dies_ing = models.BooleanField('Диагностика дизельных двигателей')
    diag_gas_ing = models.BooleanField('Диагностика бензиновых двигателей')
    diag_hybr_ing = models.BooleanField('Диагностика гибридных двигателей')
    diag_akpp = models.BooleanField('Диагностика АКПП')
    diag_fuel_sys = models.BooleanField('Диагностика топливной системы')
    diag_tnvd = models.BooleanField('Диагностика ТНВД')
    diag_turb = models.BooleanField('Диагностика турбин')
    diag_electic = models.BooleanField('Диагностика электрооборудования')

    class Meta:
        verbose_name = u""
        verbose_name_plural = u"Диагностика автомобилей"


#Ремонт КПП
class KppRepairWork(AutoserviceWork):
    autoservice = models.OneToOneField(AutoService, related_name='kpp_repair_work')
    rep_mkpp = models.BooleanField('Ремонт МКПП')
    diag_akpp = models.BooleanField('Ремонт АКПП')
    repl_mkpp = models.BooleanField('Замена МКПП')
    repl_clutch = models.BooleanField('Замена сцепления')
    repl_transf_case = models.BooleanField('Ремонт раздаточной коробки')
    repl_oil_akpp = models.BooleanField('Замена масла в АКПП')

    class Meta:
        verbose_name = u""
        verbose_name_plural = u"Ремонт КПП"


#Кондиционер, радиаторы
class AirConditionRepairWork(AutoserviceWork):
    autoservice = models.OneToOneField(AutoService, related_name='air_condition_repair_work')
    fill_cond = models.BooleanField('Заправка кондиционеров')
    rep_cond = models.BooleanField('Ремонт кондиционеров')
    argon_welding = models.BooleanField('Аргонная сварка')
    rep_rad = models.BooleanField('Ремонт радиаторов')

    class Meta:
        verbose_name = u""
        verbose_name_plural = u"Кондиционер, радиаторы"


#Автостекла
class AutoglassesRepairWork(AutoserviceWork):
    autoservice = models.OneToOneField(AutoService, related_name='autoglasses_repair_work')
    repl_autoglass = models.BooleanField('Замена автостекол')
    rep_cracks = models.BooleanField('Ремонт сколов и трещин')
    tint_autoglass = models.BooleanField('Тонировка автостекол')
    man_blind = models.BooleanField('Изготовление автошторок')

    class Meta:
        verbose_name = u""
        verbose_name_plural = u"Автостекла"


#Газовое оборудование
class GasAppliancesRepairWork(AutoserviceWork):
    autoservice = models.OneToOneField(AutoService, related_name='gas_appliances_repair_work')
    rep_gas_applian = models.BooleanField('Установка, ремонт газ. оборудования')
    train_drivers = models.BooleanField('Обучение водителей ГБО')
    crimp_cylin_gbo = models.BooleanField('Опрессовка баллонов ГБО')
    exam_cylin_gbo = models.BooleanField('Освидетельствование баллонов ГБО')

    class Meta:
        verbose_name = u""
        verbose_name_plural = u"Газовое оборудование"


#Замена масла, ремней
class OilReplaceWork(AutoserviceWork):
    autoservice = models.OneToOneField(AutoService, related_name='oil_replace_work')
    repl_oil = models.BooleanField('Замена масла, фильтров')
    repl_oil_akkp = models.BooleanField('Замена масла в АКПП')

    class Meta:
        verbose_name = u""
        verbose_name_plural = u"Замена масла"


#Аудио, Сигнализации
class AudioAlarmRepairWork(AutoserviceWork):
    autoservice = models.OneToOneField(AutoService, related_name='audio_alarm_repair_work')
    inst_audio = models.BooleanField('Установка автомагнитол, видео')
    inst_alarm = models.BooleanField('Установка втосигнализации')
    keys_imba = models.BooleanField('Ключи с иммобилайзером')
    inst_search = models.BooleanField('Установка поисковых систем')

    class Meta:
        verbose_name = u""
        verbose_name_plural = u"Аудио, Сигнализации"


#Тюнинг
class TuningWork(AutoserviceWork):
    autoservice = models.OneToOneField(AutoService, related_name='tuning_work')
    tun_salon = models.BooleanField('Перетяжка салона')
    tun_body = models.BooleanField('Тюнинг кузова')
    aerography = models.BooleanField('Аэрография')
    tun_range = models.BooleanField('Тюнинг фар')
    tun_exhaust_sys = models.BooleanField('Тюнинг выхлопной системы')
    tun_ing = models.BooleanField('Тюнинг двигателя')
    insulation = models.BooleanField('Шумоизоляция')
    past_auto_film = models.BooleanField('Оклейка авто пленкой')

    class Meta:
        verbose_name = u""
        verbose_name_plural = u"Тюнинг"


#Прочее
class OtherAutogWork(AutoserviceWork):
    autoservice = models.OneToOneField(AutoService, related_name='other_auto_work')
    man_rugs = models.BooleanField('Изготовление ковриков')
    man_covers = models.BooleanField('Изготовление чехлов')
    tun_salon = models.BooleanField('ремонт рулевой рейки')
    tun_body = models.BooleanField('ремонт сажевого фильтра')
    aerography = models.BooleanField('ремонт глушителей')
    tun_range = models.BooleanField('ремонт печек')
    tun_exhaust_sys = models.BooleanField('отопители webasto')
    rep_gydro = models.BooleanField('Ремонт гидроусилителя')
    inst_farcop = models.BooleanField('Установка Фаркопа')
    red_dv = models.BooleanField('Ремонт дворников')


    class Meta:
        verbose_name = u""
        verbose_name_plural = u"Прочее"

    # def get_work_dict(self):
    #     electrician_list = ['comp_diag', 'rep_elect', 'rep_gen']
    #     work_dict = {'Автоэлектрика': self.get_list(electrician_list),
    #                  'Кузовной ремонт': [
    #         [self._meta.get_field("car_paint").verbose_name, self.car_paint],
    #         [self._meta.get_field("rec_geo").verbose_name, self.rec_geo],
    #         [self._meta.get_field("body_work").verbose_name, self.body_work],
    #         [self._meta.get_field("welding").verbose_name, self.welding],
    #         [self._meta.get_field("select_paint").verbose_name, self.select_paint],
    #         [self._meta.get_field("rep_bump").verbose_name, self.rep_bump],
    #         [self._meta.get_field("rep_paint").verbose_name, self.rep_paint],
    #         [self._meta.get_field("sand_blasting").verbose_name, self.sand_blasting],
    #         [self._meta.get_field("cor_treatment").verbose_name, self.cor_treatment]
    #                 ]
    #     }
    #     return work_dict
    #
    # def get_list(self, f_list):
    #     f_list = [[self._meta.get_field(field).verbose_name, self.__dict__[field]] for field in f_list if self.__dict__[field]]
    #     return f_list



class TireServiceWork(models.Model):
    pass


class CarWashWork(models.Model):
    pass
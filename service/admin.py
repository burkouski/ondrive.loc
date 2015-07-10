# -*- coding: utf-8 -*-
from django.contrib import admin
from service.models import AutoService,RepairWork, SpecializationWork, ServWork, AddWork, DiagWork
from service.models import CarWash, TypeCarWash, TypeVehicle, CarWashServices, AddServices
from service.models import TireService, TireWork, DiscWork
from reviews.models import Review
from django.contrib.contenttypes.admin import GenericTabularInline


class ReviewsInline(GenericTabularInline):
    model = Review


class AutoServiceAdmin(admin.ModelAdmin):
    filter_horizontal = ('repair_work','diag_work','add_work', 'serv_work', 'specialization_work', 'add_services')
    fieldsets = (
        ('Контактные данные', {
            'fields': (
                'name', 'alias', 'address', 'site_url', 'email', 'get_logo_img', 'logo', 'phone_velcom',
                'phone_velcom2', 'phone_mts', 'phone_mts2', 'phone_life', 'phone_life2', 'phone_city', 'phone_city2', 'owner')
        }),
        ('Рабочие дни', {
            'fields': ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
        }),
        ('Время работы', {
            'fields': (
                'work_start', 'work_end', 'break_time_start', 'break_time_end', 'holiday_time_start',
                'holiday_time_end', 'holiday')
        }),
        ('Описание сервиса', {
            'fields': ('teaser', 'full_desc', 'is_top')
        }),
        ('Координаты для карты', {
            'fields': ('latitude', 'longitude')
        }),
        ('Виды работ', {
            'fields': ('repair_work','diag_work','add_work', 'serv_work', 'specialization_work', 'add_services')
        }),
        ('Мета данные', {
            'fields': ('title', 'meta_keywords', 'meta_description')
        }),

    )
    inlines = [ReviewsInline]
    readonly_fields = ('get_logo_img',)



class CarWashAdmin(admin.ModelAdmin):
    #filter_horizontal = ('type_carwash', 'type_vehicle', 'car_wash_services', 'add_services')
    fieldsets = (
        ('Контактные данные', {
            'fields': (
                'name', 'alias', 'address', 'site_url', 'email', 'get_logo_img', 'logo', 'phone_velcom',
                'phone_velcom2', 'phone_mts', 'phone_mts2', 'phone_life', 'phone_life2', 'phone_city', 'phone_city2')
        }),
        ('Рабочие дни', {
            'fields': ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
        }),
        ('Время работы', {
            'fields': (
                'work_start', 'work_end', 'break_time_start', 'break_time_end', 'holiday_time_start',
                'holiday_time_end', 'holiday')
        }),
        ('Описание сервиса', {
            'fields': ('teaser', 'full_desc', 'is_top')
        }),
        ('Координаты для карты', {
            'fields': ('latitude', 'longitude')
        }),
        ('Виды работ', {
            'fields': ('type_carwash', 'type_vehicle', 'car_wash_services', 'add_services')
        }),
        ('Мета данные', {
            'fields': ('title', 'meta_keywords', 'meta_description')
        }),

    )
    inlines = [ReviewsInline]
    readonly_fields = ('get_logo_img',)


class TireServiceAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Контактные данные', {
            'fields': (
                'name', 'alias', 'address', 'site_url', 'email', 'get_logo_img', 'logo', 'phone_velcom',
                'phone_velcom2', 'phone_mts', 'phone_mts2', 'phone_life', 'phone_life2', 'phone_city', 'phone_city2')
        }),
        ('Рабочие дни', {
            'fields': ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
        }),
        ('Время работы', {
            'fields': (
                'work_start', 'work_end', 'break_time_start', 'break_time_end', 'holiday_time_start',
                'holiday_time_end', 'holiday')
        }),
        ('Описание сервиса', {
            'fields': ('teaser', 'full_desc', 'is_top')
        }),
        ('Координаты для карты', {
            'fields': ('latitude', 'longitude')
        }),
        ('Виды работ', {
            'fields': ('tire_work', 'disc_work', 'add_services')
        }),
        ('Мета данные', {
            'fields': ('title', 'meta_keywords', 'meta_description')
        }),

    )
    #filter_horizontal = ('tire_work', 'disc_work', 'add_services')
    inlines = [ReviewsInline]
    readonly_fields = ('get_logo_img',)

admin.site.register(AutoService, AutoServiceAdmin)
admin.site.register(RepairWork)
admin.site.register(DiagWork)
admin.site.register(ServWork)
admin.site.register(AddWork)
admin.site.register(SpecializationWork)
admin.site.register(CarWash, CarWashAdmin)
admin.site.register(TypeCarWash)
admin.site.register(TypeVehicle)
admin.site.register(CarWashServices)
admin.site.register(AddServices)
#admin.site.register(AutoServiceWork, AutoServiceWorkAdmin)
admin.site.register(TireService, TireServiceAdmin)
admin.site.register(TireWork)
admin.site.register(DiscWork)


from django.contrib import admin
from service.models import AutoService, TireService, CarWash, ElectricianWork, BodyRepairWork, TireServiceWork, CarWashWork
from django.contrib.contenttypes.admin import GenericTabularInline


class ElectricianWorkInline(admin.StackedInline):
    model = ElectricianWork


class BodyRepairWorkInline(admin.StackedInline):
    model = BodyRepairWork


class AutoServiceAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Контактные данные', {
            'fields': (
            'name', 'alias', 'address', 'site_url', 'email', 'get_logo_img', 'logo',)
        }),
        ('Рабочие дни', {
            'fields': ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
        }),
        ('Время работы', {
            'fields': (
            'work_start', 'work_end', 'break_time_start', 'break_time_end', 'holiday_time_start', 'holiday_time_end', 'holiday')
        }),
        ('Описание сервиса', {
            'fields': ('teaser', 'full_desc', 'is_top')
        }),
        ('Координаты для карты', {
            'fields': (('latitude', 'longitude'))
        }),
        ('Мета данные', {
            'fields': ('title', 'meta_keywords', 'meta_description')
        }),

    )
    readonly_fields = ('get_logo_img',)
    inlines = [
        ElectricianWorkInline,
        BodyRepairWorkInline
    ]


class TireServiceAdmin(admin.ModelAdmin):
    inlines = [
        #AutoServiceWorkInline
    ]


class IngredientAdmin(admin.ModelAdmin):
    pass


class CarWashAdmin(admin.ModelAdmin):
    inlines = [
        #AutoServiceWorkInline
    ]



admin.site.register(AutoService, AutoServiceAdmin)
#admin.site.register(TireService, TireServiceAdmin)
#admin.site.register(CarWash, CarWashAdmin)
#admin.site.register(AutoServiceWork, AutoServiceWorkAdmin)



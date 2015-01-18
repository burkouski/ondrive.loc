from django.contrib import admin
from service.models import AutoService, TireService, CarWash, AutoServiceWork, TireServiceWork, CarWashWork
from django.contrib.contenttypes.admin import GenericTabularInline


class AutoServiceWorkInline(admin.StackedInline):
    model = AutoServiceWork
    fieldsets = (
        ('АвтоЭлектрика', {
            'fields': ('comp_diag', 'rep_elect', 'rep_gen')
        }),
        ('Кузовной ремонт', {
            'fields': ('car_paint', 'rec_geo', 'body_work', 'welding', 'select_paint', 'rep_bump', 'rep_paint','sand_blasting', 'cor_treatment')
        })
    )


class AutoServiceAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Контактные данные', {
            'fields': (
            'name', 'alias', 'address', 'site_url', 'email', ('work_start', 'work_end'), 'get_logo_img', 'logo',)
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
        AutoServiceWorkInline
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



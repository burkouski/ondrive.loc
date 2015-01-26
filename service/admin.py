from django.contrib import admin
from service.models import AutoService, ElectricianWork, BodyRepairWork, EngineRepairWork,FuelSystemRepairWork, SuspensionRepairWork, BreakSystemRepairWork, AutoDiagWork, KppRepairWork,AirConditionRepairWork,AutoglassesRepairWork,GasAppliancesRepairWork,OilReplaceWork,AudioAlarmRepairWork, TuningWork, OtherAutogWork
from django.contrib.contenttypes.admin import GenericTabularInline



class BodyRepairWorkInline(admin.StackedInline):
    model = BodyRepairWork


class AutoServiceAdmin(admin.ModelAdmin):
    filter_horizontal = ('electrician_work', 'body_repair_work', 'engine_repair_work', 'fuel_system_repair_work', 'suspension_repair_work', 'break_system_repair_work', 'auto_diag_work',
            'kpp_repair_work', 'air_condition_repair_work', 'autoglasses_repair_work', 'gas_applianses_repair_work', 'oil_replace_work', 'audio_alarm_repair_work', 'tuning_work', 'other_auto_work')
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
            'fields': ('latitude', 'longitude')
        }),
        ('Виды работ', {
            'fields': ('electrician_work', 'body_repair_work', 'engine_repair_work', 'fuel_system_repair_work', 'suspension_repair_work', 'break_system_repair_work', 'auto_diag_work',
            'kpp_repair_work', 'air_condition_repair_work', 'autoglasses_repair_work', 'gas_applianses_repair_work', 'oil_replace_work', 'audio_alarm_repair_work', 'tuning_work', 'other_auto_work')
        }),
        ('Мета данные', {
            'fields': ('title', 'meta_keywords', 'meta_description')
        }),

    )
    readonly_fields = ('get_logo_img',)


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
admin.site.register(ElectricianWork)
admin.site.register(BodyRepairWork)
admin.site.register(EngineRepairWork)
admin.site.register(FuelSystemRepairWork)
admin.site.register(SuspensionRepairWork)
admin.site.register(BreakSystemRepairWork)
admin.site.register(AutoDiagWork)
admin.site.register(KppRepairWork)
admin.site.register(AirConditionRepairWork)
admin.site.register(AutoglassesRepairWork)
admin.site.register(GasAppliancesRepairWork)
admin.site.register(OilReplaceWork)
admin.site.register(AudioAlarmRepairWork)
admin.site.register(TuningWork)
admin.site.register(OtherAutogWork)
#admin.site.register(TireService, TireServiceAdmin)
#admin.site.register(CarWash, CarWashAdmin)
#admin.site.register(AutoServiceWork, AutoServiceWorkAdmin)



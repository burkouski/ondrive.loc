from tastypie.resources import ModelResource
from tastypie import fields
from service.models import AutoService, AutoServiceWork


class TopAutoserviceRes(ModelResource):
    class Meta:
        queryset = AutoService.objects.filter(is_top=True)
        resource_name = 'autoserviceTop'
        excludes = ['phone_city',
                    #'id',
                    'title',
                    'phone_mts',
                    'phone_velcom',
                    'phone_life',
                    'work_start',
                    'work_end',
                    'monday',
                    'tuesday',
                    'thursday',
                    'wednesday',
                    'friday',
                    'saturday',
                    'sunday',
                    'meta_keywords',
                    'meta_description',
                    'alias',
                    'email',
                    'full_desc',
                    'site_url',
                    'logo',
                    'is_top', ]


class AutoserviceRes(ModelResource):
    workTypes = fields.ForeignKey('service.api.AutoserviceWorkRes', 'autoservice',  full=True, null=True)
    url = fields.CharField(attribute='get_absolute_url', readonly=True)

    class Meta:
        queryset = AutoService.objects.all()
        resource_name = 'allAutoservice'
        excludes = ['phone_city',
                    'id',
                    'title',
                    'phoneMts',
                    'phone_velcom',
                    'phone_life',
                    'work_start',
                    'work_end',
                    'monday',
                    'tuesday',
                    'thursday',
                    'wednesday',
                    'friday',
                    'saturday',
                    'sunday',
                    'meta_keywords',
                    'meta_description',
                    'alias',
                    'email',
                    'full_desc',
                    'site_url',
                    'is_top', ]


class AutoserviceWorkRes(ModelResource):
    #service = fields.ToManyField('app.service.api.TopAutoserviceRes', 'entry')

    class Meta:
        queryset = AutoServiceWork.objects.all()
        resource_name = 'autoserviceWork'

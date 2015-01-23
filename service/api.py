from tastypie.resources import ModelResource
from tastypie import fields
from service.models import AutoService, ElectricianWork, BodyRepairWork
from itertools import chain


class TopAutoserviceRes(ModelResource):
    class Meta:
        queryset = AutoService.objects.filter(is_top=True)
        resource_name = 'autoservices_top'
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
    work_list = fields.ListField(attribute='get_work_list', readonly=True)

    class Meta:
        queryset = AutoService.objects.all()
        resource_name = 'autoservices'
        excludes = ['phone_city',
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
                    'is_top', ]



class ElectricianWorkRes(ModelResource):
    class Meta:
        queryset = ElectricianWork.objects.all()
        resource_name = 'electrician_work'
        excludes = ['id', 'resource_uri']


class BodyRepairWorkRes(ModelResource):

    class Meta:
        queryset = BodyRepairWork.objects.all()
        resource_name = 'body_repair_work'

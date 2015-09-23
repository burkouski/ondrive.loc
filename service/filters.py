import django_filters
from rest_framework import filters
from service.models import AutoService

class AutoserviceFilter(django_filters.FilterSet):
    class Meta:
        model = AutoService
        fields = ['specialization_work']

# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, get_list_or_404, render, HttpResponse
from service.models import AutoService, CarWash, TireService
from service.serializers import AutoserviceSerializer, CarWashSerializer, TireServiceSerializer
from django.db.models import Avg
from django.apps import apps
from django.contrib.contenttypes.models import ContentType
import json
from itertools import chain
from django.views.decorators.csrf import ensure_csrf_cookie
import re
import ast
from rest_framework import generics, permissions, filters


class AutoserviceList(generics.ListCreateAPIView):
    serializer_class = AutoserviceSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def get_queryset(self):
        queryset = AutoService.objects.all()
        filter = self.request.query_params.getlist('filter', None)
        if filter  != []:
            queryset = filtering(filter, queryset)
        return queryset


class CarWashList(generics.ListCreateAPIView):
    serializer_class = CarWashSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def get_queryset(self):
        queryset = CarWash.objects.all()
        filter = self.request.query_params.getlist('filter', None)
        if filter != []:
            queryset = filtering(filter, queryset)
        return queryset


class TireServiceList(generics.ListCreateAPIView):
    serializer_class = TireServiceSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def get_queryset(self):
        queryset = TireService.objects.all()
        filter = self.request.query_params.getlist('filter', None)
        if filter  != []:
            queryset = filtering(filter, queryset)
        return queryset

# @ensure_csrf_cookie
def service_list(request):
    if request.GET.get('_escaped_fragment_') == '':
        autoservice = AutoService.objects.all()
        carwash = CarWash.objects.all()
        tireservice = TireService.objects.all()
        services = list(chain(autoservice, carwash, tireservice))
        return render(request, 'service/sns-service_list.html', {'services': services})
    if request.method == 'POST':
        post_data = json.loads(request.body)
        services = AutoService.objects.all()
        services = filtering(request.POST, services)
        return HttpResponse(services)

    return render(request, 'service/service_list.html')


def autoservice_detail(request, service_alias):
    service = get_object_or_404(AutoService, alias=service_alias)
    args = get_service_ctx(AutoService, service)
    return render(request, 'service/autoservice_detail_view.html', args)


@ensure_csrf_cookie
def autoservice_list(request):
    if request.GET.get('_escaped_fragment_') == '':
        services = AutoService.objects.all()
        return render(request, 'service/sns_autoservice_list_view.html', {'services': services})
    if request.method == 'POST':
        post_data = json.loads(request.body)
        services = AutoService.objects.all()
        services = filtering(post_data, services)
        return HttpResponse(services)

    return render(request, 'service/autoservice_list_view.html')


def autoservice_filter(request,filter_name, filter_alias):
    args = {}
    model_name = re.sub('[_]', '', filter_name)
    z = ContentType.objects.get(model=model_name)
    ModelB = apps.get_model(z.app_label, model_name)
    filter = get_object_or_404(ModelB , alias=filter_alias)
    args = {'filter_name': filter_name, 'filter_alias': filter_alias, 'filter': filter}
    return render(request, 'service/autoservice_list_view.html', args)


#################### АВТОМОЙКИ ####################


def carwash_detail(request, service_alias):
    service = get_object_or_404(CarWash, alias=service_alias)
    args = get_service_ctx(CarWash, service)
    return render(request, 'service/carwash_detail_view.html', args)


@ensure_csrf_cookie
def carwash_list(request):
    if request.GET.get('_escaped_fragment_') == '':
        services = CarWash.objects.all()
        return render(request, 'service/sns_carwash_list_view.html', {'services': services})

    if request.method == 'POST':
        post_data = json.loads(request.body)
        services = CarWash.objects.all()
        services = filtering(post_data, services)
        return HttpResponse(services)
    return render(request, 'service/carwash_list_view.html')

def carwash_filter(request,filter_name, filter_alias):
    args = {}
    model_name = re.sub('[_]', '', filter_name)
    z = ContentType.objects.get(model=model_name)
    ModelB = apps.get_model(z.app_label, model_name)
    filter = get_object_or_404(ModelB , alias=filter_alias)
    args = {'filter_name': filter_name, 'filter_alias': filter_alias, 'filter': filter}
    return render(request, 'service/carwash_list_view.html', args)
#################### ШИНОМОНТАЖИ ####################

def tireservice_detail(request, service_alias):
    service = get_object_or_404(TireService, alias=service_alias)
    args = get_service_ctx(TireService, service)
    return render(request, 'service/tireservice_detail_view.html', args)


@ensure_csrf_cookie
def tireservice_list(request):
    if request.GET.get('_escaped_fragment_') == '':
        services = TireService.objects.all()
        return render(request, 'service/sns_tireservice_list_view.html', {'services': services})
    if request.method == 'POST':
        post_data = json.loads(request.body)
        services = TireService.objects.all()
        services = filtering(post_data, services)
        return HttpResponse(services)
    return render(request, 'service/tireservice_list_view.html')

def tireservice_filter(request,filter_name, filter_alias):
    args = {}
    model_name = re.sub('[_]', '', filter_name)
    z = ContentType.objects.get(model=model_name)
    ModelB = apps.get_model(z.app_label, model_name)
    filter = get_object_or_404(ModelB , alias=filter_alias)
    args = {'filter_name': filter_name, 'filter_alias': filter_alias, 'filter': filter}
    return render(request, 'service/tireservice_list_view.html', args)


# фильтрация объектов
def filtering(filter, queryset):
    filter = ast.literal_eval(filter[0])
    queryset = queryset
    for key, val in filter.items():
        for item in val:
            queryset = queryset.filter(**{key: item})
    queryset = queryset.annotate(sort=Avg('reviews__rate')).order_by('-sort')
    return queryset



# получение контекста для детального описания сервиса
def get_service_ctx(service, object):
    rel = service._meta.get_m2m_with_model()
    reviews = object.reviews.filter(is_moderate=True)
    rating = reviews.aggregate(Avg('rate'))
    args = {'service': object, 'rel': rel, 'rating': rating, 'reviews': reviews}
    return args

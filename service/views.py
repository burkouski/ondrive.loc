# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, get_list_or_404, render, HttpResponse
from service.models import AutoService, CarWash, TireService
from django.db.models import Avg
from django.apps import apps
from django.contrib.contenttypes.models import ContentType
import json
from itertools import chain
from django.views.decorators.csrf import ensure_csrf_cookie
import re


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


# фильтрация объектов
def filtering(post_data, objects):
    obj = {}
    quantity = 6
    page = 1
    print post_data
    if post_data.get(u'meta'):
        quantity = post_data[u'meta'][u'quantity']
        page = post_data[u'meta'][u'page']
        print(quantity)
    if post_data.get(u'options'):
        options = post_data[u'options']
        for key in options:
            obj[key] = options[key]
        for key, val in obj.items():
            for x in val:
                objects = objects.filter(**{key: x})
    objects = objects.annotate(sort=Avg('reviews__rate')).order_by('-sort')
    map_objects = objects
    objects = {
        'info': [{
                     'name': o.name,
                     'logo': o.logo.url,
                     'teaser': o.teaser,
                     'city': o.city,
                     'address': o.address,
                     'building': o.building,
                     'rating': o.get_rating(),
                     'sort': o.sort,
                     'url': o.get_absolute_url()} for o in objects[(quantity * page):(quantity * page + quantity)]],

        'meta': objects.count()
    }
    map_objects = [{
                       'name': o.name,
                       'longitude': o.longitude,
                       'latitude': o.latitude,
                       'teaser': o.teaser,
                       'city': o.city,
                       'address': o.address,
                       'building': o.building,
                       'sort': o.sort,
                       'url': o.get_absolute_url()} for o in map_objects]

    a = json.dumps(
        {'objects': objects, 'mapObjects': map_objects}
    )
    return a


# получение контекста для детального описания сервиса
def get_service_ctx(service, object):
    rel = service._meta.get_m2m_with_model()
    reviews = object.reviews.filter(is_moderate=True)
    rating = reviews.aggregate(Avg('rate'))
    args = {'service': object, 'rel': rel, 'rating': rating, 'reviews': reviews}
    return args

from django.shortcuts import get_object_or_404, get_list_or_404, render, HttpResponse
from service.models import AutoService, CarWash, TireService
from django.db.models import Avg
import json
from django.views.decorators.csrf import ensure_csrf_cookie


def autoservice_detail(request, service_alias):
    service = get_object_or_404(AutoService, alias=service_alias)
    args = get_service_ctx(AutoService, service)
    return render(request, 'service/autoservice_detail_view.html', args)


@ensure_csrf_cookie
def autoservice_list(request):
    services = AutoService.objects.all()
    services = filtering(request.POST, services)

    if request.method == 'POST':
        return HttpResponse(services)

    return render(request, 'service/autoservice_list_view.html')


#################### АВТОМОЙКИ ####################

def carwash_detail(request, service_alias):
    service = get_object_or_404(CarWash, alias=service_alias)
    args = get_service_ctx(CarWash, service)
    return render(request, 'service/carwash_detail_view.html', args)

@ensure_csrf_cookie
def carwash_list(request):
    services = CarWash.objects.all()
    services = filtering(request.POST, services)

    if request.method == 'POST':
        return HttpResponse(services)

    return render(request, 'service/carwash_list_view.html')


#################### ШИНОМОНТАЖИ ####################

def tireservice_detail(request, service_alias):
    service = get_object_or_404(TireService, alias=service_alias)
    args = get_service_ctx(TireService, service)
    return render(request, 'service/tireservice_detail_view.html', args)

@ensure_csrf_cookie
def tireservice_list(request):
    services = TireService.objects.all()
    services = filtering(request.POST, services)

    if request.method == 'POST':
        return HttpResponse(services)

    return render(request, 'service/tireservice_list_view.html')


# фильтрация объектов
def filtering(post_data, objects):
    obj = {}
    for key in post_data:
        obj[key[:-2]] = post_data.getlist(key)

    for key, val in obj.items():
        for x in val:
            objects = objects.filter(**{key: x})
    objects = objects.annotate(sort=Avg('reviews__rate')).order_by('-sort')
    objects = json.dumps(
        {
        'info': [{
                            'name': o.name,
                            'longitude': o.longitude,
                            'latitude': o.latitude,
                            'logo': o.logo.url,
                            'teaser': o.teaser,
                            'address': o.address,
                            'rating': o.reviews.filter(is_moderate=True).aggregate(Avg('rate'))['rate__avg'],
                            'sort': o.sort,
                            'url': o.get_absolute_url()} for o in objects],
        'meta': objects.count()
        })
    return objects


# получение контекста для детального описания сервиса
def get_service_ctx(service, object):
    rel = service._meta.get_m2m_with_model()
    reviews = object.reviews.filter(is_moderate=True)
    rating = reviews.aggregate(Avg('rate'))
    args = {'service': object, 'rel': rel, 'rating': rating, 'reviews': reviews}
    return args

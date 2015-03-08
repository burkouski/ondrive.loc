from django.shortcuts import get_object_or_404, get_list_or_404, render, HttpResponse
from service.models import AutoService,CarWash, ElectricianWork
from django.db.models import Avg
import json
from django.views.decorators.csrf import ensure_csrf_cookie


def autoservice_detail(request, service_alias):
    service = get_object_or_404(AutoService, alias=service_alias)
    rel = AutoService._meta.get_m2m_with_model()
    reviews = service.reviews.filter(is_moderate=True)
    rating = reviews.aggregate(Avg('rate'))
    args = {'service': service, 'rel': rel, 'rating': rating, 'reviews': reviews}
    return render(request, 'service/detail_view.html', args)

@ensure_csrf_cookie
def autoservice_list(request):
    services = AutoService.objects.all()
    obj = {}
    for key in request.POST:
        obj[key[:-2]] = request.POST.getlist(key)

    for key, val in obj.items():
        for x in val:
            services = services.filter(**{key: x})
    services = services.annotate(sort=Avg('reviews__rate')).order_by('-sort')
    services = json.dumps(
        {
        'info': [{
                            'name': o.name,
                            'longitude': o.longitude,
                            'latitude': o.latitude,
                            'logo': o.logo.url,
                            'teaser': o.teaser,
                            'address': o.address,
                            'rating': o.reviews.all().aggregate(Avg('rate'))['rate__avg'],
                            'sort': o.sort,
                            'url': o.get_absolute_url()} for o in services],
        'meta': services.count()
        }),

    if request.method == 'POST':
        return HttpResponse(services)

    return render(request, 'service/autoservice_list_view.html')



@ensure_csrf_cookie
def autoservice_top(request):
    services = AutoService.objects.filter(is_top=True)[:5]
    services = json.dumps([{
                            'name': o.name,
                            'longitude': o.longitude,
                            'latitude': o.latitude,
                            'logo': o.logo.url,
                            'teaser': o.teaser,
                            'address': o.address,
                            'url': o.get_absolute_url()} for o in services])
    if request.method == 'POST':
        return HttpResponse(services)


#################### АВТОМОЙКИ ####################

def carwash_detail(request, service_alias):
    service = get_object_or_404(CarWash, alias=service_alias)
    rel = CarWash._meta.get_m2m_with_model()
    reviews = service.reviews.filter(is_moderate=True)
    rating = reviews.aggregate(Avg('rate'))
    args = {'service': service, 'rel': rel, 'rating': rating, 'reviews': reviews}
    return render(request, 'service/detail_view.html', args)

@ensure_csrf_cookie
def carwash_list(request):
    services = CarWash.objects.all()
    obj = {}
    for key in request.POST:
        obj[key[:-2]] = request.POST.getlist(key)

    for key, val in obj.items():
        for x in val:
            services = services.filter(**{key: x})
    services = services.annotate(sort=Avg('reviews__rate')).order_by('-sort')
    services = json.dumps(
        {
        'info': [{
                            'name': o.name,
                            'longitude': o.longitude,
                            'latitude': o.latitude,
                            'logo': o.logo.url,
                            'teaser': o.teaser,
                            'address': o.address,
                            'rating': o.reviews.all().aggregate(Avg('rate'))['rate__avg'],
                            'sort': o.sort,
                            'url': o.get_absolute_url()} for o in services],
        'meta': services.count()
        }),

    if request.method == 'POST':
        return HttpResponse(services)

    return render(request, 'service/carwash_list_view.html')

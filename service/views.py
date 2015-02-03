from django.shortcuts import get_object_or_404, get_list_or_404, render, HttpResponse
from service.models import AutoService, ElectricianWork
import json
from django.views.decorators.csrf import ensure_csrf_cookie


def autoservice_detail(request, service_alias):
    service = get_object_or_404(AutoService, alias=service_alias)
    rel = AutoService._meta.get_m2m_with_model()

    args = {'service': service, 'rel': rel}
    return render(request, 'service/detail_view.html', args)

@ensure_csrf_cookie
def autoservice_list(request):
    services = AutoService.objects.all()
    obj = {}
    for key in request.POST:
        obj[key[:-2]] = request.POST.getlist(key)

    for key, val in obj.items():
        for x in val:
            services = services.filter(**{ key: x })

    services = json.dumps([{
        #'dls': obj,
                            'name': o.name,
                            'longitude': o.longitude,
                            'latitude': o.latitude,
                            'logo': o.logo.url,
                            'teaser': o.teaser,
                            'address': o.address,
                            'url': o.get_absolute_url()} for o in services])
    if request.method == 'POST':
        return HttpResponse(services)

    return render(request, 'service/list_view.html')
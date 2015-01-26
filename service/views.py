from django.shortcuts import get_object_or_404, get_list_or_404, render
from service.models import AutoService, ElectricianWork
from django.core import serializers

def autoservice_detail(request, service_alias):
    service = get_object_or_404(AutoService, alias=service_alias)

    args = {'service': service}
    return render(request, 'service/detail_view.html', args)


def autoservice_list(request):
    services = get_list_or_404(AutoService)
    return render(request, 'service/list_view.html', {'services': services})
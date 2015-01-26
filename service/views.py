from django.shortcuts import get_object_or_404, get_list_or_404, render
from service.models import AutoService, ElectricianWork
from django.core import serializers

def autoservice_detail(request, service_alias):
    service = get_object_or_404(AutoService, alias=service_alias)

    args = {'service': service}
    return render(request, 'service/detail_view.html', args)


def autoservice_list(request):
    services = AutoService.objects.filter(electrician_work__in= [1,2], body_repair_work__in=[1,2]).distinct()
    services = serializers.serialize('json',services)
    return render(request, 'service/list_view.html', {'services': services})
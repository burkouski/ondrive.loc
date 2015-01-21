from django.shortcuts import get_object_or_404, get_list_or_404, render
from service.models import AutoService, AutoServiceWork


def autoservice_detail(request, service_alias):
    service = get_object_or_404(AutoService, alias=service_alias)
    works = AutoServiceWork.objects.get(autoservice=service.id)
    args = {'service': service, 'works': works}
    return render(request, 'service/detail_view.html', args)


def autoservice_list(request):
    services = get_list_or_404(AutoService)
    return render(request, 'service/list_view.html', {'services': services})
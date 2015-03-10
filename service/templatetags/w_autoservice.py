from django import template
from service.models import AutoService, CarWash
from django.template import RequestContext
register = template.Library()


@register.inclusion_tag("service/w_autoservice.html")
def show_top_autoservice():
    service_list = AutoService.objects.filter(is_top='true')
    return {'service_list': service_list}

@register.inclusion_tag("service/w_filter.html")
def show_autoservice_filter():
    res = {}
    njson = AutoService._meta.get_m2m_with_model()
    json = [x[0].rel.to for x in njson]
    for y in json:
        res[y._meta.verbose_name_plural.title()] = y.objects.all()
    return {'res': res, 'nj': njson, 'filter_name': 'asFilter'}

@register.inclusion_tag("service/w_filter.html")
def show_carwash_filter():
    res = {}
    njson = CarWash._meta.get_m2m_with_model()
    json = [x[0].rel.to for x in njson]
    for y in json:
        res[y._meta.verbose_name_plural.title()] = y.objects.all()
    return {'res': res, 'nj': njson, 'filter_name': 'cwFilter'}
from django import template
from service.models import AutoService

register = template.Library()


@register.inclusion_tag("service/w_autoservice.html")
def show_top_autoservice():
    service_list = AutoService.objects.filter(is_top='true')
    return {'service_list': service_list}
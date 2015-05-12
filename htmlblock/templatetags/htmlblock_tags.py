from htmlblock.models import Htmlblock
from django import template


register = template.Library()


@register.inclusion_tag("htmlblock/w-htmlblock.html")
def show_htmlblock(label):
    object = Htmlblock.objects.get(label=label)
    args = {'object': object}
    return args

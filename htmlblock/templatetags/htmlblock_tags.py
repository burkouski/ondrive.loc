from htmlblock.models import Htmlblock, MetaData
from django import template


register = template.Library()


@register.inclusion_tag("htmlblock/w-htmlblock.html")
def show_htmlblock(label):
    object = Htmlblock.objects.get(label=label)
    args = {'object': object}
    return args


@register.simple_tag(takes_context=True)
def show_page_title(context, label):
    object = MetaData.objects.get(label=label)
    context['metaData'] = object

    return ''


# @register.inclusion_tag()
# def show_page_descpription(label):
#     object = MetaData.objects.get(label=label)
#     args = {'object': object}
#     return args

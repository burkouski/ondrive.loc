from django_hosts import patterns, host
from django.views.generic import TemplateView

host_patterns = patterns('',
    host(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    host(r'(foo|bar)', 'service.urls', name='autoservice_list'),
)
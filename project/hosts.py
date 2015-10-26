from django_hosts import patterns, host
from django.conf import settings

host_patterns = patterns('',
    host(r'', settings.ROOT_URLCONF, name='default'),
    host(r'autoservices', 'service.urls', name='autoservices'),
    #host(r'^autoservices/(?P<service_alias>.*)/$', 'service.urls', name='autoservices'),
)
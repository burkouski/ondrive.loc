from django_hosts import patterns, host
from django.conf import settings

host_patterns = patterns('',
    host(r'', settings.ROOT_URLCONF, name='default'),
    host(r'autoservices', 'service.urls.as_urls', name='autoservices'),
    host(r'carwashes', 'service.urls.cw_urls', name='carwashes'),
    host(r'tireservices', 'service.urls.ts_urls', name='tireservices'),
    #host(r'^autoservices/(?P<service_alias>.*)/$', 'service.urls', name='autoservices'),
)
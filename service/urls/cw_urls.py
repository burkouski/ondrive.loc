from django.conf.urls import patterns, url,include
from service import views
from django.conf import settings

urlpatterns = patterns('service.views',
    url(r'^$', views.carwash_list, name='carwash_list'),
    url(r'^api/', include('service.urls.api_urls', namespace='api')),
    url(r'^(?P<service_alias>.*)/$', views.carwash_detail, name='carwash_detail'),
    url(r'^carwash/(?P<filter_name>.*)/(?P<filter_alias>.*)/$', views.carwash_filter, name='carwash_filter'),
    # url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

)

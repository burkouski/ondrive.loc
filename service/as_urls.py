from django.conf.urls import patterns, url, include
from service import views
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', views.autoservice_list, name='autoservice_list'),
    url(r'^autoservice/(?P<filter_name>.*)/(?P<filter_alias>.*)/$', views.autoservice_filter, name='autoservice_filter'),
     url(r'^api/autoservice/$', views.AutoserviceList.as_view(), name='autoservice_api_list'),
    url(r'^(?P<service_alias>.*)/$', views.autoservice_detail, name='autoservice_detail'),
    #url(r'', include('service.api_urls', namespace='service')),

    #url(r'^api/tireservice/$', views.CarWashList.as_view(), name='carwash_api_list'),
    #url(r'^api/tireservice/$', views.TireServiceList.as_view(), name='tireservice_api_list'),
    # url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

)

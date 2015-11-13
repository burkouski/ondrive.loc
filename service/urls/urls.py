from django.conf.urls import patterns, url
from service import views
from django.views.generic import TemplateView

urlpatterns = patterns('service.views',
    url(r'^$', views.service_list,  name="service_list"),
    url(r'^autoservices/$', views.autoservice_list, name='autoservice_list'),
    url(r'^autoservice/(?P<filter_name>.*)/(?P<filter_alias>.*)/$', views.autoservice_filter, name='autoservice_filter'),
    url(r'^autoservice/(?P<service_alias>.*)/$', views.autoservice_detail, name='autoservice_detail'),
    url(r'^carwash/$', views.carwash_list, name='carwash_list'),
    url(r'^carwash/(?P<filter_name>.*)/(?P<filter_alias>.*)/$', views.carwash_filter, name='carwash_filter'),
    url(r'^carwash/(?P<service_alias>.*)/$', views.carwash_detail, name='carwash_detail'),
    url(r'^tireservice/$', views.tireservice_list, name='tireservice_list'),
    url(r'^tireservice/(?P<filter_name>.*)/(?P<filter_alias>.*)/$', views.tireservice_filter, name='tireservice_filter'),
    url(r'^tireservice/(?P<service_alias>.*)/$', views.tireservice_detail, name='tireservice_detail'),
    url(r'^api/autoservice/$', views.AutoserviceList.as_view(), name='autoservice_api_list'),
    url(r'^api/carwash/$', views.CarWashList.as_view(), name='carwash_api_list'),
    url(r'^api/tireservice/$', views.TireServiceList.as_view(), name='tireservice_api_list'),
    # url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

)
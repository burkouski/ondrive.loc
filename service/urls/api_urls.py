from django.conf.urls import patterns, url
from service import views
from django.conf import settings

urlpatterns = patterns('service.views',
    url(r'^autoservice/$', views.AutoserviceList.as_view(), name='autoservice_api_list'),
    url(r'^carwash/$', views.CarWashList.as_view(), name='carwash_api_list'),
    url(r'^tireservice/$', views.TireServiceList.as_view(), name='tireservice_api_list'),
    # url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

)

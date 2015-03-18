from django.conf.urls import patterns, url
from service import views

urlpatterns = patterns('service.views',
    url(r'^autoservices/$', views.autoservice_list, name='autoservice_list'),
    url(r'^autoservice/(?P<service_alias>.*)/$', views.autoservice_detail, name='autoservice_detail'),
    url(r'^carwash/$', views.carwash_list, name='carwash_list'),
    url(r'^carwash/(?P<service_alias>.*)/$', views.carwash_detail, name='carwash_detail'),
    url(r'^tireservice/$', views.tireservice_list, name='tireservice_list'),
    url(r'^tireservice/(?P<service_alias>.*)/$', views.tireservice_detail, name='tireservice_detail')

)

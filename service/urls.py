from django.conf.urls import patterns, url

from service import views

urlpatterns = patterns('service.views',
    url(r'^api/topautoservices/$', views.autoservice_top, name='autoservice_top'),
    url(r'^autoservices/$', views.autoservice_list, name='autoservice_list'),
    url(r'^autoservice/(?P<service_alias>.*)/$', views.autoservice_detail, name='autoservice_detail'),
    #url(r'^api/topcarwash/$', views.carwash_top, name='carwash_top'),
    url(r'^carwash/$', views.carwash_list, name='carwash_list'),
    url(r'^carwash/(?P<service_alias>.*)/$', views.carwash_detail, name='carwash_detail')

)

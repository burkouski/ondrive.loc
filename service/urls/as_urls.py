from django.conf.urls import patterns, url, include
from service import views
from django.conf import settings
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', views.autoservice_list, name='autoservice_list'),
    url(r'^api/', include('service.urls.api_urls', namespace='api')),
    url(r'^auth/', include('myauth.urls', namespace='myauth'), name='auth'),
    url(r'^reviews/', include('reviews.urls', namespace='reviews')),
    url(r'^(?P<service_alias>.*)/$', views.autoservice_detail, name='autoservice_detail'),
    url(r'^autoservice/(?P<filter_name>.*)/(?P<filter_alias>.*)/$', views.autoservice_filter, name='autoservice_filter'),

)

from django.conf.urls import patterns, url, include
from service import views
from django.conf import settings

urlpatterns = patterns('service.views',
    url(r'^$', views.tireservice_list, name='tireservice_list'),
    url(r'^api/', include('service.urls.api_urls', namespace='api')),
    url(r'^auth/', include('myauth.urls', namespace='myauth'), name='auth'),
    url(r'^reviews/', include('reviews.urls', namespace='reviews')),
    url(r'^(?P<service_alias>.*)/$', views.tireservice_detail, name='tireservice_detail'),
    url(r'^tireservice/(?P<filter_name>.*)/(?P<filter_alias>.*)/$', views.tireservice_filter, name='tireservice_filter'),
    # url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

)

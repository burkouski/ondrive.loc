from django.conf.urls import patterns, include, url
from django.http import HttpResponse
from django.conf import settings

urlpatterns = patterns('',
                       url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': settings.MEDIA_ROOT}),
                       url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': settings.STATIC_ROOT}), )

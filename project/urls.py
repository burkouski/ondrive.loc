from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
from tastypie.api import Api

#from app.service.api import AutoserviceRes, TopAutoserviceRes, AutoserviceWorkRes


# v1_api = Api(api_name='v1')
# v1_api.register(TopAutoserviceRes())
# v1_api.register(AutoserviceRes())
# v1_api.register(AutoserviceWorkRes())


urlpatterns = patterns('',
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    #url(r'', include('app.service.urls', namespace='service')),
    #url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^news/', include('news.urls', namespace='news')),
    url(r'^auth/', include('myauth.urls', namespace='myauth')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    #url(r'^api/', include(v1_api.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)

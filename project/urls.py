from django.conf.urls import patterns, include, url
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib import admin
from django.conf import settings
from pages import views
from news.sitemap import NewsPostSitemap, NewsCategorySitemap
from service.sitemap import *


sitemaps = {'news_posts': NewsPostSitemap,
            'news_category': NewsCategorySitemap,
            'autoseservice': AutoServicetSitemap,
            'SpecializationWork': SpecializationWorkSitemap,
            'RepairWorkSitemap':RepairWorkSitemap,
            'DiagWorkSitemap': DiagWorkSitemap,
            'ServWorkSitemap': ServWorkSitemap,
            'AddWorkSitemap': AddWorkSitemap,
            'carwash': CarWashSitemap,
            'tireservice': TireServiceSitemap,
            'typecarwash': TypeCarWashSitemap,
            'typevehicle': TypeVehicleSitemap,
            'carwashservice': CarWashServicesSitemap,
            'tireservice': TireServiceSitemap,
            'tirework': TireWorkSitemap,
            'discwork': DiagWorkSitemap
            }


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    #url(r'^services/', include('service.urls', namespace='service')),
    url(r'', include('contacts.urls', namespace='contacts')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^news/', include('news.urls', namespace='news')),
    url(r'^tuning/', include('tuning.urls', namespace='tuning')),
    url(r'^reviews/', include('reviews.urls', namespace='reviews')),
    url(r'^auth/', include('myauth.urls', namespace='myauth')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^(?P<page_alias>.*)/$', views.get_page, name='page_view'),
    url(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /admin/",content_type='text/plain')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
)

admin.autodiscover()
#admin.site.unregister(User)

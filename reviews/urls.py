from django.conf.urls import patterns, url

from reviews import views

urlpatterns = patterns('service.views',
    url(r'^api/createreview/$', views.create_review, name='create_review'),

)

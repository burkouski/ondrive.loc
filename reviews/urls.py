from django.conf.urls import patterns, url

from reviews import views

urlpatterns = patterns('service.views',
    url(r'^api/sendreview/$', views.send_review, name='send_review'),

)

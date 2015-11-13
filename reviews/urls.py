from django.conf.urls import patterns, url
from reviews import views

urlpatterns = patterns('',
    url(r'^api/createreview/$', views.create_review, name='create_review'),
    #url(r'^api/createreview/$', views.ReviewList.as_view(), name='show_review'),

)

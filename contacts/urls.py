from django.conf.urls import patterns, url
from contacts import views

urlpatterns = patterns('service.views',
    url(r'^contacts/$', views.contacts_view, name='contacts'),
    url(r'^cooperate/$', views.contacts_view, name='contacts'),
    url(r'^api/sendmessage/$', views.send_message, name='send_message'),
    #url(r'^cooperate/$', views.cooperate_view, name='cooperate'),
)

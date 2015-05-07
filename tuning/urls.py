from django.conf.urls import patterns, url
from tuning.views import get_post_list, get_post_detail

urlpatterns = patterns('tuning.views',
    url(r'^$', get_post_list, name='tuning_post_list'),
    url(r'^(?P<post_alias>.*)/$', get_post_detail, name='tuning_post_detail')
)
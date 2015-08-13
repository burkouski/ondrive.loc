from django.conf.urls import patterns, url
from news.views import get_post_list, get_post_detail, get_category_posts
urlpatterns = patterns('news.views',
    url(r'^$', get_post_list, name='post_list'),
    url(r'^(?P<category_alias>\w+)/(?P<post_alias>[\w-]+)/$', get_post_detail, name='post_detail'),
    url(r'^(?P<category_alias>\w+)/$', get_category_posts, name='category_post_list'),
)
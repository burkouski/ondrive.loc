from django.conf.urls import patterns, include, url
from news.views import get_post_list, get_post_detail, get_category_posts
urlpatterns = patterns('news.views',
    # Examples:
    # url(r'^$', 'djangonotes.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', get_post_list, name='post_list'),
    url(r'^(?P<category_alias>\w+)/$', get_category_posts, name='category_post_list'),
    url(r'^(?P<category_alias>\w+)/(?P<post_alias>[\w-]+)/$', get_post_detail, name='post_detail'),
    #url(r'^tags/(?P<tag_alias>\w+)/$', TagPostListView.as_view(), name='tag_posts_list'),
    #url(r'^archive/$', ArchivePostsView.as_view(), name='archive_posts_list'),

    #url(r'^(?P<category_alias>\w+)/(?P<post_alias>[\w-]+)/$', PostDetailView.as_view(), name='post_detail'),



)
from django.conf.urls import patterns, include, url
from myauth.views import register
urlpatterns = patterns('news.views',
    # Examples:
    # url(r'^$', 'djangonotes.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^registration/$', register, name='register'),
    #url(r'^(?P<category_alias>\w+)/$', get_category_posts, name='category_post_list'),
    #url(r'^(?P<category_alias>\w+)/(?P<post_alias>[\w-]+)/$', get_post_detail, name='post_detail'),
    #url(r'^tags/(?P<tag_alias>\w+)/$', TagPostListView.as_view(), name='tag_posts_list'),
    #url(r'^archive/$', ArchivePostsView.as_view(), name='archive_posts_list'),

    #url(r'^(?P<category_alias>\w+)/(?P<post_alias>[\w-]+)/$', PostDetailView.as_view(), name='post_detail'),



)

from django.conf.urls import patterns, include, url
from myauth.views import user_register, user_login, user_logout
from django.views.generic import TemplateView

urlpatterns = patterns('news.views',
    # Examples:
    # url(r'^$', 'djangonotes.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^registration/$', user_register, name='user_register'),
    url(r'^registration/success/$', TemplateView.as_view(template_name='myauth/success.html')),
    url(r'^login/$', user_login, name='user_login'),
    url(r'^logout/$', user_logout, name='user_logout'),
    #url(r'^(?P<category_alias>\w+)/$', get_category_posts, name='category_post_list'),
    #url(r'^(?P<category_alias>\w+)/(?P<post_alias>[\w-]+)/$', get_post_detail, name='post_detail'),
    #url(r'^tags/(?P<tag_alias>\w+)/$', TagPostListView.as_view(), name='tag_posts_list'),
    #url(r'^archive/$', ArchivePostsView.as_view(), name='archive_posts_list'),

    #url(r'^(?P<category_alias>\w+)/(?P<post_alias>[\w-]+)/$', PostDetailView.as_view(), name='post_detail'),



)

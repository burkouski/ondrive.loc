from django.conf.urls import patterns, include, url
from myauth.views import user_register, user_login, user_logout, user_confirm, user_board, userprofile_edit,userprofile_service, autoservice_edit, carwash_edit, tireservice_edit
from django.views.generic import TemplateView

urlpatterns = patterns('news.views',
    # Examples:
    # url(r'^$', 'djangonotes.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^registration/$', user_register, name='user_register'),
    #url(r'^registration/success/$', TemplateView.as_view(template_name='myauth/success.html')),
    url(r'^registration/(?P<activation_key>\w+)/', user_confirm, name='user_confirm'),
    url(r'^login/$', user_login, name='user_login'),
    url(r'^logout/$', user_logout, name='user_logout'),
    url(r'^user/$', user_board, name='user_board'),
    url(r'^user/edit/$', userprofile_edit, name='userprofile_edit'),
    url(r'^user/service/$', userprofile_service, name='userprofile_service'),
    url(r'^user/service/edit_as_(?P<service_id>\w+)/$', autoservice_edit, name='autoservice_edit'),
    url(r'^user/service/edit_cw_(?P<service_id>\w+)/$', carwash_edit, name='carwash_edit'),
    url(r'^user/service/edit_ts_(?P<service_id>\w+)/$', tireservice_edit, name='tireservice_edit'),
    #url(r'^(?P<category_alias>\w+)/$', get_category_posts, name='category_post_list'),
    #url(r'^(?P<category_alias>\w+)/(?P<post_alias>[\w-]+)/$', get_post_detail, name='post_detail'),
    #url(r'^tags/(?P<tag_alias>\w+)/$', TagPostListView.as_view(), name='tag_posts_list'),
    #url(r'^archive/$', ArchivePostsView.as_view(), name='archive_posts_list'),

    #url(r'^(?P<category_alias>\w+)/(?P<post_alias>[\w-]+)/$', PostDetailView.as_view(), name='post_detail'),



)

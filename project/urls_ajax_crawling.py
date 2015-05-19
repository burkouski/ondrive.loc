from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index2.html')),
)

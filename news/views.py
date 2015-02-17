from django.shortcuts import get_object_or_404,get_list_or_404, render
from news.models import Post, Category
from news.disqus import get_disqus_sso


def _get_disqus_sso(user):
    if user.is_authenticated():
        disqus_sso = get_disqus_sso(user)
    else:
        disqus_sso = get_disqus_sso()
    return disqus_sso


def count_post_views(request, post):
    if request.method == 'GET':
        post.views = post.views + 1
        post.save()


def get_post_list(request):
    posts = get_list_or_404(Post)
    args = {'posts': posts}
    return render(request, 'news/news_list_view.html', args)


def get_category_posts(request, category_alias):
    category_id = get_object_or_404(Category, alias=category_alias).id
    posts = get_list_or_404(Post, category=category_id)
    args = {'posts': posts}
    return render(request, 'news/news_list_view.html', args)


def get_post_detail(request, category_alias, post_alias):
    category_id = get_object_or_404(Category, alias=category_alias).id
    post = get_object_or_404(Post, category=category_id, alias=post_alias)
    count_post_views(request, post)
    disqus_sso = _get_disqus_sso(request.user)
    args = {'post': post,'disqus_sso': disqus_sso}
    return render(request, 'news/news_detail_view.html', args)
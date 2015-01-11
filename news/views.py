from django.shortcuts import get_object_or_404,get_list_or_404, render
from news.models import Post, Category


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
    args = {'post': post}
    return render(request, 'news/news_detail_view.html', args)
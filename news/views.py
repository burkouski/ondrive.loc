from django.shortcuts import get_object_or_404,get_list_or_404, render
from news.models import Post, Category


def count_post_views(request, post):
    if request.method == 'GET':
        post.views = post.views + 1
        post.save()


def get_post_list(request):
    posts = get_list_or_404(Post)
    args = {'posts': posts}
    return render(request, 'news/news_list_view.html', args)


def get_category_posts(request, category_alias):
    category = get_object_or_404(Category, alias=category_alias)
    category_id = category.id
    posts = get_list_or_404(Post, category=category_id)
    args = {'posts': posts, 'category': category}
    return render(request, 'news/news_list_view.html', args)


def get_post_detail(request, category_alias, post_alias):
    category_id = get_object_or_404(Category, alias=category_alias).id
    post = get_object_or_404(Post, category=category_id, alias=post_alias)
    count_post_views(request, post)
    args = {'post': post}
    return render(request, 'news/news_detail_view.html', args)
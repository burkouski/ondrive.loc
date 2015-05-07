from django.shortcuts import get_object_or_404,get_list_or_404, render
from tuning.models import Post


def count_post_views(request, post):
    if request.method == 'GET':
        post.views = post.views + 1
        post.save()

def get_post_list(request):
    posts = get_list_or_404(Post)
    args = {'posts': posts}
    return render(request, 'tuning/tuning_list_view.html', args)


# Create your views here.
def get_post_detail(request, post_alias):
    post = get_object_or_404(Post, alias=post_alias)
    count_post_views(request, post)
    args = {'post': post}
    return render(request, 'tuning/tuning_detail_view.html', args)

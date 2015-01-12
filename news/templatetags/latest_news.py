from django import template
from news.models import Post

register = template.Library()


@register.inclusion_tag("news/w_latest_news.html")
def show_latest_news():
    posts = Post.objects.all()[:8]
    args = {'posts': posts}
    return args
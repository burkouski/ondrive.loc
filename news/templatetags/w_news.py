from django import template
from news.models import Post, Category

register = template.Library()


@register.inclusion_tag("news/w_latest_news.html")
def show_latest_news():
    posts = Post.objects.all()[:6]
    args = {'posts': posts}
    return args

@register.inclusion_tag("news/w_categories.html")
def show_categories():
    categories = Category.objects.all()
    args = {'categories': categories}
    return args
import base64
import hashlib
import hmac
import json
import time
from django import template
from tuning.models import Post
from django import template
from django.conf import settings


register = template.Library()


@register.inclusion_tag("tuning/w_videos.html")
def show_videos():
    objects = Post.objects.exclude(video__isnull=True)[:5]
    args = {'objects': objects}
    return args
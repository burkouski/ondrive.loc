import base64
import hashlib
import hmac
import json
import time
from django import template
from news.models import Post, Category
from django import template
from django.conf import settings


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


@register.simple_tag(takes_context=True)
def disqus_sso(context, callback_func="null"):
    """
    Return the HTML/js code to enable DISQUS SSO - so logged in users on
    your site can be logged in to disqus seemlessly.
    """
    DISQUS_SECRET_KEY = getattr(settings, 'DISQUS_SECRET_KEY', None)
    if DISQUS_SECRET_KEY is None:
        return "<p>You need to set DISQUS_SECRET_KEY before you can use SSO</p>"
    DISQUS_PUBLIC_KEY = getattr(settings, 'DISQUS_PUBLIC_KEY', None)
    if DISQUS_PUBLIC_KEY is None:
        return "<p>You need to set DISQUS_PUBLIC_KEY before you can use SSO</p>"

    # we have to make it bytes rather than string(unicode) or the HMAC blows up
    DISQUS_SECRET_KEY = bytes(DISQUS_SECRET_KEY, 'ascii')
    DISQUS_PUBLIC_KEY = bytes(DISQUS_PUBLIC_KEY, 'ascii')
    user = context['user']
    if user.is_anonymous():
        return """function disqus_config() {
this.sso = {
            name: "ondrive.by",
            button: "https://a.disquscdn.com/dotcom/d-221b350/img/logos/logo-navbar-blue.png",
            icon: "https://a.disquscdn.com/dotcom/d-221b350/img/logos/logo-navbar-blue.png",
            url: "http:/localhost:8000/auth/login/",
            logout: "http:/localhost:8000/auth/logout/",
            width: "800",
            height: "400"
        };
}"""
    # create a JSON packet of our data attributes
    data = json.dumps({
        'id': user.id,
        'username': user.username,
        'email': user.email,
    })
    # encode the data to base64
    message = base64.b64encode(bytes(data, 'ascii'))
    # generate a timestamp for signing the message
    timestamp = int(time.time())
    input_data = bytes('%s %s' % (message.decode(), timestamp), 'ascii')
    # generate our hmac signature
    sig = hmac.HMAC(DISQUS_SECRET_KEY, input_data, hashlib.sha1).hexdigest()

    #return 'a script tag to insert the sso message'
    return """function disqus_config() {
this.page.remote_auth_s3 = "%(message)s %(sig)s %(timestamp)s";
this.page.api_key = "%(pub_key)s";
this.sso = {
            name: "ondrive.by",
            button: "https://a.disquscdn.com/dotcom/d-221b350/img/logos/logo-navbar-blue.png",
            icon: "https://a.disquscdn.com/dotcom/d-221b350/img/logos/logo-navbar-blue.png",
            url: "http:/localhost:8000/auth/login/",
            logout: "http:/localhost:8000/auth/logout/",
            width: "800",
            height: "400"
        };
this.callbacks.onNewComment = [%(callback_func)s];

}""" % dict(
        message=message.decode(),
        timestamp=timestamp,
        sig=sig,
        pub_key=DISQUS_PUBLIC_KEY.decode(),
        callback_func=callback_func,
    )
from django.contrib.sitemaps import Sitemap
from news.models import Post, Category


class NewsPostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return Post.objects.filter().order_by('pk')

    def lastmod(self, obj):
        return obj.lastmod

    # def location(self, obj):
    #     return "/node/%s/" % obj.id
class NewsCategorySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return Category.objects.filter().order_by('pk')

    def lastmod(self, obj):
        return obj.lastmod
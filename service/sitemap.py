from django.contrib.sitemaps import Sitemap
from service.models import *


class AutoServicetSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return AutoService.objects.filter().order_by('pk')

    def lastmod(self, obj):
        return obj.lastmod

    # def location(self, obj):
    #     return "/node/%s/" % obj.id
class CarWahSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return CarWah.objects.filter().order_by('pk')

    def lastmod(self, obj):
        return obj.lastmod


class SpecializationWorkSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return SpecializationWork.objects.filter().order_by('pk')

    def lastmod(self, obj):
        return obj.lastmod


class RepairWorkSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return RepairWork.objects.filter().order_by('pk')

    def lastmod(self, obj):
        return obj.lastmod

class DiagWorkSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return DiagWork.objects.filter().order_by('pk')

    def lastmod(self, obj):
        return obj.lastmod


class ServWorkSitemap(Sitemap):
    changefreq = 'allways'
    priority = 0.5

    def items(self):
        return ServWork.objects.filter().order_by('pk')

    def lastmod(self, obj):
        return obj.lastmod


class AddWorkSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return AddWork.objects.filter().order_by('pk')

    def lastmod(self, obj):
        return obj.lastmod
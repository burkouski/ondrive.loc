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

class CarWashSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return CarWash.objects.filter().order_by('pk')

    def lastmod(self, obj):
        return obj.lastmod


class TypeCarWashSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return TypeCarWash.objects.filter().order_by('pk')

    def lastmod(self, obj):
        return obj.lastmod


class TypeVehicleSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return TypeVehicle.objects.filter().order_by('pk')

    def lastmod(self, obj):
        return obj.lastmod


class CarWashServicesSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return CarWashServices.objects.filter().order_by('pk')

    def lastmod(self, obj):
        return obj.lastmod



class TireServiceSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return TireService.objects.filter().order_by('pk')

    def lastmod(self, obj):
        return obj.lastmod

class TireWorkSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return TireWork.objects.filter().order_by('pk')

    def lastmod(self, obj):
        return obj.lastmod


class DiscWorkSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return DiscWork.objects.filter().order_by('pk')

    def lastmod(self, obj):
        return obj.lastmod
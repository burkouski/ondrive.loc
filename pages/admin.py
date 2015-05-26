# -*- coding: utf-8 -*-
from django.contrib import admin
from pages.models import Page


# Register your models here.
class PageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Page, PageAdmin)
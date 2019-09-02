# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Search


class SearchAdmin(admin.ModelAdmin):
    search_display = ('label', 'favorites', 'image_url', 'directions_url',
                      'ingredients', 'calories', 'total time')


# Register your models here.
admin.site.register(Search, SearchAdmin)

# -*- coding: utf-8 -*-
from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from src.apps.effect_log import models


class EffectLogAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_created'
    list_display = ('category', 'operator', 'type_prostoy', 'time_prostoy','dlitelnost_prostoya','comments',
                    'user_name')
    list_filter = ['user_name']
    search_fields = ['description']


class CategoryAdmin(DjangoMpttAdmin):
    list_display = ('name', 'is_active')
    fieldsets = ((None, {'fields': ('name', 'is_active', 'parent', 'description', 'user_name')}), )
    search_fields = ('name',)
    mptt_level_indent = 20

admin.site.register(models.EffectLog, EffectLogAdmin)
admin.site.register(models.Category, CategoryAdmin)

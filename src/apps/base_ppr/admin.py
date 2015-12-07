# -*- coding: utf-8 -*-
from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from src.apps.base_ppr import models

class CategoryAdmin(DjangoMpttAdmin):
    list_display = ('name', 'is_active', 'user_name')
    fieldsets = ((None, {'fields': ('name', 'is_active', 'parent', 'user_name')}), )
    search_fields = ('name',)
    mptt_level_indent = 20


class ActionAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_created'
    list_display = ('title', 'category', 'date_created', 'date_updated', 'user_name',)
    list_filter = ['category', 'date_created', 'user_name']
    search_fields = ['title']


class ActionHistoryAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_created'
    list_display = ('title', 'action', 'date_created', 'date_updated', 'user_name',)
    list_filter = ['user_name', 'date_created',]
    search_fields = ['title']

admin.site.register(models.ActionHistory, ActionHistoryAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Action, ActionAdmin)

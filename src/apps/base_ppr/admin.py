from django.contrib import admin

from src.apps.base_ppr import models

class PlanAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_created'
    list_display = ('user_name', 'priority', 'description_action', 'date_created', 'date_updated')
    list_filter = ['priority', 'user_name']
    search_fields = ['description_action']


admin.site.register(models.Plan, PlanAdmin)

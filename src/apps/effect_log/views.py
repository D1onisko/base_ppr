# -*- coding: utf-8 -*-
from django.views.generic import DetailView, TemplateView, ListView
from django.shortcuts import get_object_or_404, redirect

from src.apps.effect_log.models import Category, EffectLog


"""
Index page
"""
class EffectLogIndexView(ListView):
    template_name = 'apps/effect_log/effect_index.html'
    model = EffectLog

    def get_queryset(self):
        return EffectLog.objects.all()

class EffectLogList(ListView):
    template_name = 'apps/effect_log/effect_log_in_category.html'
    model = EffectLog
    context_object_name = 'log_vivod'

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['slug'])

        # filter product in child category
        if category.is_child_node():
            return EffectLog.objects.filter(category_id=category.pk)
        # view all product in root category
        elif category.is_root_node():
            q = category.get_children()
            t = q.values('id')
            x = [item['id'] for item in t]
            return EffectLog.objects.filter(category_id__in=x)
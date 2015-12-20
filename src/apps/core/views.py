# -*- coding: utf-8 -*-
from django.views.generic import DetailView, TemplateView, ListView
from django.shortcuts import get_object_or_404, redirect


"""
Index page
"""
class CoreIndexView(TemplateView):
    template_name = 'apps/core/index.html'

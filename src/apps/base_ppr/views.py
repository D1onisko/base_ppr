# -*- coding: utf-8 -*-
from django.views.generic import DetailView, TemplateView, ListView
from django.shortcuts import get_object_or_404, redirect

from src.apps.base_ppr.models import TestIndex

"""
Index page
"""
class IndexView(TemplateView):
    template_name = 'base.html'

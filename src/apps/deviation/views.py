# -*- coding: utf-8 -*-
from django.views.generic import DetailView, TemplateView, ListView
from django.shortcuts import get_object_or_404, redirect


"""
Index page
"""
class IndexView(TemplateView):
    template_name = 'base.html'

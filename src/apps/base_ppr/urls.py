# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from src.apps.base_ppr.views import IndexView

from src.apps.base_ppr import views

urlpatterns = [

    url(r'^$', IndexView.as_view(), name='base_ppr'),

]

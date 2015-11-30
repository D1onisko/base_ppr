# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from src.apps.base_ppr.views import IndexView


urlpatterns = patterns('src.apps.base_ppr.views',

    url(r'^$', IndexView.as_view(), name='base_ppr'),

)

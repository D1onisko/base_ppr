# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from src.apps.core.views import CoreIndexView


urlpatterns = patterns('src.apps.core.views',

    url(r'', CoreIndexView.as_view(), name='index'),

)

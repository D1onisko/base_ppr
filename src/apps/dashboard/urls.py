# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from src.apps.dashboard.views import DashboardIndexView, EffectLogWrite


urlpatterns = patterns('src.apps.dashboard.views',

    url(r'^accounts/profile/', DashboardIndexView.as_view(), name='dashboard_index'),
    url(r'accounts/write/$', EffectLogWrite.as_view(), name='effect_log_write'),

)

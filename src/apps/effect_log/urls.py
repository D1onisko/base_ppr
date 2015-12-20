# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from src.apps.effect_log.views import EffectLogIndexView, EffectLogList


urlpatterns = patterns('src.apps.effect_log.views',

    url(r'^index/', EffectLogIndexView.as_view(), name='effect_log_index'),
    url(r'^(?P<slug>[^/]+)/$', EffectLogList.as_view(), name='effect_log_in_category'),

)

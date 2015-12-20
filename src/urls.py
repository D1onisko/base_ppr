from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),

    url(r'^effect_log/', include('src.apps.effect_log.urls', namespace='effect_log')),
    url(r'^dashboard/', include('src.apps.dashboard.urls', namespace='dashboard')),
    url(r'^', include('src.apps.core.urls', namespace='core')),

]

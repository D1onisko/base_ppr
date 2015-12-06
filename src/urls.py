from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('src.apps.base_ppr.urls', namespace='base_ppr')),
]

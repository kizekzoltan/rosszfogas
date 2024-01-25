"""
    Fő URL konfiguráció
    @package rosszfogas
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Applikáció URL előtag
    path('', include('default.urls')),
    path('fiok/', include('account.urls')),
    path('hirdetesek/', include('shop.urls')),
]

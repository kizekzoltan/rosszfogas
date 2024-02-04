"""
    Fő URL konfiguráció
    @package rosszfogas
"""
from django.contrib import admin
from django.urls import path, include

from django.conf .urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # Applikáció URL előtag
    path('', include('default.urls')),
    path('fiok/', include('account.urls')),
    path('hirdetesek/', include('shop.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
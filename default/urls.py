"""
    URL konfiguráció a statikus oldalakhoz
    @package rosszfogas
"""
from django.urls import path
from . import views

urlpatterns = [
    # Views
    path('', views.index_view, name="fooldal"),
    path('rolunk/', views.about_us_view, name="roulnk"),
    path('forum/', views.forum_view, name="forum"),
]
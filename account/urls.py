"""
    URL konfiguráció a fiók oldalakhoz
    @package rosszfogas
"""
from django.urls import path
from . import views

urlpatterns = [
    # Views
    path('', views.profile_view, name="fiok"),
    path('regisztracio/', views.register_view, name="regisztracio"),
    path('bejelentkezes/', views.login_view, name="bejelentkezes"),
]
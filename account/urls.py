"""
    URL konfiguráció a fiók oldalakhoz
    @package rosszfogas
"""
from django.urls import path
from . import views

urlpatterns = [
    # Views
    path('', views.profile_view, name="fiok"),
    path('regisztracio/', views.register, name="regisztracio"),
    path('bejelentkezes/', views.user_login, name="bejelentkezes"),
    path('logout/', views.logout_view, name='logout'),
]
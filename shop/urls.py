"""
    URL konfiguráció a hirdetes oldalakhoz
    @package rosszfogas
"""
from django.urls import path
from . import views

urlpatterns = [
    # Views
    path('', views.shop_view, name="hirdetesek"),
    path('hirdetes/<str:product_name>', views.product_view, name="hirdetes"),
    path('letrehozas/', views.hirdetes_letrehozasa, name="hirdetes_letrehozasa"),
    path('fizetes/', views.payment_view, name="fizetes"),
]
"""
    URL konfiguráció a statikus oldalakhoz
    @package rosszfogas
"""
from django.urls import path
from . import views

urlpatterns = [
    # Views
    path('', views.shop, name="shop"),
    path('kosar/', views.kosar, name="kosar"),
    path('checkout/', views.checkout, name="checkout"),
    path('<str:item_name>.html', views.item_detail, name='item_detail'),
]
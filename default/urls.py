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
    path('<int:product_id>.html', views.item_detail, name='item_detail'),
    path('update_item/', views.updateItem, name="update_item"),
    path('gyik/', views.gyik, name="gyik"),
    path('product/<int:product_id>/order/', views.order, name='order'),
    path('product/<int:product_id>/place_order/', views.place_order, name='place_order'),
    path('orders/', views.orders, name='orders'),
    path('rolunk/', views.rolunk, name='rolunk'),
]
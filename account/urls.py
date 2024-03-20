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
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('delete_customer/<int:customer_id>/', views.delete_customer, name='delete_customer'),
    path('forum', views.forum_cucc, name="forumcucc"),
    path('topic/<int:topic_id>/', views.topic_detail, name="topic_detail"),
    path('delete_topic/<int:topic_id>/', views.delete_topic, name='delete_topic'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('sending/<int:product_id>', views.send_order, name='send_order'),
]

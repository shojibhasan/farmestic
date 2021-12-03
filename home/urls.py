from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all_products/', views.all_products, name='all_products'),
    path('post_product/', views.post_product, name='post_product'),
    path('product_details/<int:id>/', views.product_details, name='product_details'),
    path('product_bid/', views.product_bid, name='product_bid'),
    path('bids/', views.show_bids, name='product_bid_details'),
    path('contact/', views.contact, name='contact'),
]

from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all_products/', views.all_products, name='all_products'),
    path('post_product/', views.post_product, name='post_product'),
    path('product_details/<int:id>/', views.product_details, name='product_details'),
    path('product_bid/', views.product_bid, name='product_bid'),
    path('bids/<int:id>', views.show_bids, name='product_bid_details'),
    path('contact/', views.contact, name='contact'),
    path('profile/',views.profile,name="profile"),
    path('delete/<int:product_id>',views.delete,name="delete_product"),
    path('seller/<int:id>',views.seller_profile,name="seller_profile"),
    path("edit_products/<int:id>",views.edit_product,name="edit_products"),
    path('search/',views.product_search,name='search'),
]

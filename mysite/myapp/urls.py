from django.contrib import admin
from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    
    path('', views.index),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('products/<int:pk>', views.ProductDetailView.as_view(), name='product_details'),
    path('products/add/', views.ProductCreateView.as_view(), name='add_product'),
    path('products/update/<int:id>', views.update_product, name='update_product'),
    path('products/delete/<int:id>', views.delete_product, name='delete_product'),
    path('products/mylistings', views.my_listings, name='my_listings'),
]
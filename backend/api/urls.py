from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ProductList.as_view(), name='product-list'),
    path('create/', views.ProductCreate.as_view(), name='product-create'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout')
]
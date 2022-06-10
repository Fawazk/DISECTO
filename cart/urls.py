from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.CartItemList.as_view(),name='cart-items'),
    path('update/<int:id>', views.CartDetail.as_view(),name='update-cart'),
    path('invoice', views.invoice,name='invoice'),
]
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.ItemList.as_view(),name='items'),
    path('create-item', views.ItemCreate.as_view(),name='create-item'),
    path('item/<slug:slug>', views.ItemDetail.as_view(),name='item'),
    path('expired-items', views.ExpiredItems.as_view(),name='expired-items'),
    
]
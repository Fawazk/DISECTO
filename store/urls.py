from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.ItemList.as_view(),name='items'),
    path('item/<slug:slug>', views.ItemDetail.as_view(),name='item')
]
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from . models import ItemModel
from . serializers import ItemModelSerializer
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class ItemList(generics.ListCreateAPIView):
    queryset = ItemModel.objects.all()
    serializer_class = ItemModelSerializer
    permission_classes = [IsAuthenticated]

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ItemModel.objects.all()
    serializer_class = ItemModelSerializer
    lookup_field = 'slug'
    


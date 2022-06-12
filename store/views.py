from operator import ge
from . models import ItemModel
from . serializers import ItemModelSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAdminUser
# Create your views here.

class ItemList(generics.ListAPIView):
    """
    GET method for products (For users)
    """
    queryset = ItemModel.objects.all()
    serializer_class = ItemModelSerializer
    permission_classes = [IsAuthenticated]


class ItemCreate(generics.ListCreateAPIView):
    """
    POST and GET method for creating new products (For admin)
    """
    queryset = ItemModel.objects.all()
    serializer_class = ItemModelSerializer
    permission_classes = [IsAuthenticated,IsAdminUser]


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    GET, PUT and DELETE methods for a product (For admin)
    """
    permission_classes = [IsAuthenticated,IsAdminUser]
    queryset = ItemModel.objects.all()
    serializer_class = ItemModelSerializer
    lookup_field = 'slug'
    
class ExpiredItems(generics.ListAPIView):
    """
    GET method for expired products 
    """
    queryset = ItemModel.objects.all()
    serializer_class = ItemModelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Search for expired items only.
        """
        return ItemModel.objects.filter(is_expired=True)

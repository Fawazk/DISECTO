from datetime import date
from . models import CartItem
from . serializers import CartItemSerializer
from django.http import JsonResponse
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes

#invoice generation 
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from . utils import render_to_pdf
import os

# Create your views here.

class CartItemList(generics.ListCreateAPIView):
    """
    POST and GET method for creating 
    a cart item and listing all cart-items for the 
    currently authenticated user..
    """
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        """
        This view update user coloumn with currently
        authenticated user when post method is called.
        """
        serializer.save(user=self.request.user, )
        
    def get_queryset(self):
        """
        This view returns a list cart-items for the currently
        authenticated user.

        Returns empyt list if user Anonymous
        """
        user = self.request.user

        if not user.is_anonymous:
            return CartItem.objects.filter(user=user)

        return CartItem.objects.none()


class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    GET, UPDATE, DELETE methods for a cart item
    """
    permission_classes = [IsAuthenticated]
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    lookup_field = 'id'


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def invoice(request):
    """
    Generate invoice for the cart items available for currently authenticated user.
    """
    cartitems = CartItem.objects.filter(user=request.user)
    if not cartitems:
        return JsonResponse({'Info':'No CartItems found'})
    grandtotal = 0
    for item in cartitems:
        grandtotal += item.product.price*item.quantity
    today = date.today()
    data = {
        'cartitems': cartitems,
        'grandtotal': grandtotal,
        'user' : request.user,
        'today':today
    }
    pdf = render_to_pdf('invoice.html',data)
    return HttpResponse(pdf,content_type='application/pdf')


from . models import CartItem
from . serializers import CartItemSerializer
from django.http import HttpResponse
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.template.loader import render_to_string
# Create your views here.

class CartItemList(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user, )
        
    def get_queryset(self):
        """
        This view returns a list of all the authors for the currently
        authenticated user.

        Returns empyt list if user Anonymous
        """
        user = self.request.user

        if not user.is_anonymous:
            return CartItem.objects.filter(user=user)

        return CartItem.objects.none()

class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    lookup_field = 'id'
    
# @api_view(['GET'])
# @permission_classes([permissions.IsAuthenticated])
# def invoice(request, invoice_id):
#     invoice = get_object_or_404(Invoice, pk=invoice_id, created_by=request.user)
#     team = Team.objects.filter(created_by=request.user).first()

#     template_name = 'pdf.html'

#     if invoice.is_credit_for:
#         template_name = 'pdf_creditnote.html'

#     template = get_template(template_name)
#     html = template.render({'invoice': invoice, 'team': team})
#     pdf = pdfkit.from_string(html, False, options={})

#     response = HttpResponse(pdf, content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'

#     return response
def invoice(request):
    invoice = CartItem.objects.filter(user=request.user)
    template_path = 'invoice.html'

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'

    html = render_to_string(template_path, {'invoice': invoice})
    print (html)

    return response


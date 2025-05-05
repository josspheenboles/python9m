import rest_framework.permissions

from .serializer import *
from ..models import *
from rest_framework.response import  Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.generics import RetrieveUpdateAPIView



from django.shortcuts import get_object_or_404
@api_view(['GET'])
@authentication_classes(['BasicAuthentication'])
@permission_classes(['IsAuthenticated'])

def GetallProduct(request):
    products=Product.getall()
    Serialized_Products=Product_serializer(products,many=True)
    return Response(data=Serialized_Products.data,status=status.HTTP_200_OK)

class ProductView(APIView):
    authentication_classes = [rest_framework.authentication.BasicAuthentication]
    permission_classes = [rest_framework.permissions.IsAuthenticated]
    def get(self,request,id):
        productobj=Product.getbyid(id)
        if(productobj):
            product_serialized=Product_serializer(instance=productobj)
            print(product_serialized.data)
            return Response(data=product_serialized.data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ProductRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    """
    API endpoint that allows products to be:
    - Retrieved (GET)
    - Updated (PUT/PATCH)
    """
    permission_classes = [rest_framework.permissions.AllowAny]

    # Optimized queryset with category prefetch
    queryset = Product.objects.select_related('catagoryid').filter(isactive=True)

    serializer_class = Product_serializer
    lookup_field = 'pk'  # Using 'id' since that's your primary key
    http_method_names = ['get', 'put', 'patch', 'head', 'options']

    def perform_update(self, serializer):
        """Custom update logic with change tracking"""
        serializer.save(
            modified_by=self.request.user
        )


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('catagoryid').all()
    serializer_class = Product_serializer
    permission_classes = [rest_framework.permissions.AllowAny]
    lookup_field = 'id'
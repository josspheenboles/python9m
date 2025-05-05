from .serializer import *
from ..models import *
from rest_framework.response import  Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET'])
def GetallProduct(request):
    products=Product.getall()
    Serialized_Products=Product_serializer(products,many=True)
    return Response(data=Serialized_Products.data,status=status.HTTP_200_OK)

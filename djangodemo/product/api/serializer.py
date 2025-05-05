from rest_framework import serializers
from catagory.Serializers import Catagory_Serializer

class Product_serializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    image = serializers.ImageField()
    isactive = serializers.BooleanField(default=True)
    # Nested  Serializers
    catagoryid =Catagory_Serializer()
from rest_framework import serializers
from catagory.models import Category


class Product_serializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50, null=False, unique=False)
    image = serializers.ImageField(upload_to='product/images/', null=True, blank=True)
    isactive = serializers.BooleanField(default=True)
    catagoryid = serializers.ForeignKey(Category, on_delete=models.CASCADE)
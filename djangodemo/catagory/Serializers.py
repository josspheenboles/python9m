from rest_framework import serializers
from .models import *
class Catagory_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

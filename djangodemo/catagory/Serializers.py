from rest_framework import serializers
from .models import *
class Catagory_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        feilds='--all--'
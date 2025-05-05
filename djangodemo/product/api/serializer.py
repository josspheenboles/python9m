from rest_framework import serializers
from catagory.Serializers import Catagory_Serializer

class Product_serializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    image = serializers.ImageField()
    isactive = serializers.BooleanField(default=True)
    # Nested  Serializers
    catagoryid =Catagory_Serializer()
    def update(self, instance, validated_data):
        # Update simple fields
        instance.name = validated_data.get('name', instance.name)
        instance.isactive = validated_data.get('isactive', instance.isactive)

        # Handle image update (if provided)
        if 'image' in validated_data:
            instance.image = validated_data['image']

        # Handle category update (if provided)
        if 'catagoryid' in validated_data:
            instance.catagoryid = validated_data['catagoryid']

        instance.save()
        return instance
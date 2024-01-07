from rest_framework import serializers
from .models import StoreUploadImg

class ImageSerializer(serializers.ModelSerializer):
    
    userID = serializers.IntegerField()
    image = serializers.ImageField()
    
    class Meta:
        model = StoreUploadImg
        fields = ['userID', 'image']

# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StoreUploadImg
#         fields = '__all__'
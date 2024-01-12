from rest_framework import serializers
from .models import StoreUploadImg, LoginPicImg

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
        
class LoginImageSer(serializers.ModelSerializer):
    
    # userID = serializers.IntegerField()
    image = serializers.JSONField()
    
    class Meta:
        model = LoginPicImg
        fields = ['image']
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class Register(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user_data = User.objects.get(username=request.data['username'])
            # set_passeord==>hash the user password
            user_data.set_password(request.data['password'])
            user_data.save()
            token = Token.objects.create(user=user_data)
            return Response({"token":token.key,"user":serializer.data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Login(APIView):
    def post(self,request):
        user = get_object_or_404(User,username=request.data['username'])
        if not user.check_password(request.data['password']):
            return Response({"details":"Invalid credentials"},status=status.HTTP_404_NOT_FOUND)
        token,created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(instance=user)
        return Response({"token":token.key,"user":serializer.data})


class Validate_token(APIView):
        authentication_classes = [TokenAuthentication]
        permission_classes = [IsAuthenticated]

        def get(self,request):
            valid_user = UserSerializer(request.user).data
            response = {
                'id':valid_user['id'],
                'username': valid_user['username'],
                'email': valid_user['email']
            }
            return Response(response,status=status.HTTP_200_OK)





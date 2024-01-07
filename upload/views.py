from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from.models import StoreUploadImg
# from .serializers import PostSerializer
from rest_framework.parsers import MultiPartParser
from .models import StoreUploadImg
from .serializers import ImageSerializer
from PIL import Image
from io import BytesIO
# import requests
from django.core.files.base import ContentFile
from rest_framework import status

import os

class PostViewSet(ModelViewSet):
    queryset = StoreUploadImg.objects.all()
    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser,)

    # def post(self, request):
    #     image = request.FILES['image']
    #     post = StoreUploadImg(image=image)
    #     post.save()
    #     return Response({'image_url': post.image.url})

class ImageView(APIView):
    def get(self, request, pk):
        image_con = StoreUploadImg.objects.get(pk=pk)
        img_url = image_con.image.file.name
        print(img_url)
        return Response({'image_url': img_url}, status=status.HTTP_200_OK)
        # response = requests.get(img_url)


        # image = Image.open(BytesIO(img_url))
        # # You can resize or process the image as needed
        #
        # # Save the image to a ContentFile
        # image_io = BytesIO()
        # image.save(image_io, format='JPEG')  # Change format as needed
        # image_file = ContentFile(image_io.getvalue(), name='image.jpg')  # Change name as needed
        #
        # return Response({'image_file': image_file}, status=status.HTTP_200_OK)
        # serializer = ImageSerializer(image)
        # return Response(serializer.data)


# class upload_view(APIView):
#     def post(self, request):
#         data = request.FILES['file']
#         # files =
#         print(data)
#         save_path = "assets\imgs"
#         with open(os.path.join(save_path, data.name), "wb+") as file1:
#             for chunk in data.chunks():
#                 file1.write(chunk)
#
#         return Response("Upload successful")
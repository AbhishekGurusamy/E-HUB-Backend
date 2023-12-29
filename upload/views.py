from rest_framework.views import APIView
from rest_framework.response import Response

import os

class upload_view(APIView):
    def post(self, request):
        data = request.FILES['file']
        # files = 
        print(data)
        save_path = "assets\imgs"
        with open(os.path.join(save_path, data.name), "wb+") as file1:
            for chunk in data.chunks():
                file1.write(chunk)

        return Response("Upload successful")
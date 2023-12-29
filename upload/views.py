from rest_framework.views import APIView
from rest_framework.response import Response

import os

class upload_view(APIView):
    def get(self, request):
        data = request.data
        # files = 
        
        print(os.listdir('assets\imgs'))

        return Response("Upload successfully")
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MediaFileSerializer

class MediaUploadView(APIView):
    def post(self, request):
        serializer = MediaFileSerializer(data=request.data)
        if serializer.is_valid():
            media_file = serializer.save()
            return Response({
                "message": "File uploaded successfully!",
                "cdn_url": media_file.cdn_url
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MediaFileSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import MediaFile
from .utils import generate_bunny_token

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



class MediaFileListView(ListAPIView):
    queryset = MediaFile.objects.all().order_by('-uploaded_at')
    serializer_class = MediaFileSerializer
    
    
    
class MediaFileTokenView(RetrieveAPIView):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileSerializer

    def get(self, request, *args, **kwargs):
        media_file = self.get_object()
        if media_file.is_private:
            secure_url = generate_bunny_token(media_file.file_name)
            return Response({"secure_url": secure_url})
        return Response({"cdn_url": media_file.cdn_url})
    
    
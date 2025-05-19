from rest_framework import serializers
from .models import MediaFile

class MediaFileSerializer(serializers.ModelSerializer):
    file = serializers.FileField(write_only=True)

    class Meta:
        model = MediaFile
        fields = ['id', 'file', 'original_filename', 'cdn_url', 'file_name', 'is_private', 'uploaded_at']
        read_only_fields = ['cdn_url', 'file_name', 'uploaded_at', 'original_filename']

    def create(self, validated_data):
        file = validated_data.pop('file')
        is_private = validated_data.get('is_private', False)
        from .utils import upload_to_bunny_storage
        cdn_url, file_name = upload_to_bunny_storage(file)

        if cdn_url:
            return MediaFile.objects.create(
                original_filename=file.name,
                file_name=file_name,
                cdn_url=cdn_url,
                is_private=is_private
            )
        raise serializers.ValidationError("File upload to Bunny CDN failed.")


from django.db import models

class MediaFile(models.Model):
    original_filename = models.CharField(max_length=255)
    file_name = models.CharField(max_length=255)
    cdn_url = models.URLField()
    is_private = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.original_filename


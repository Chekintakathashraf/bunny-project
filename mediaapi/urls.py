from django.urls import path
from .views import MediaUploadView, MediaFileListView, MediaFileTokenView

urlpatterns = [
    path('upload/', MediaUploadView.as_view(), name='upload'),
    path('media/', MediaFileListView.as_view(), name='media-list'),
    path('media/<int:pk>/token/', MediaFileTokenView.as_view(), name='media-token'),

]

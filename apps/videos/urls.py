from django.urls import path
from apps.videos.views import single_video, create_video
urlpatterns = [
    path('<int:id>', single_video, name="video"),
    path('video_create/', create_video, name = 'create_video'),
]
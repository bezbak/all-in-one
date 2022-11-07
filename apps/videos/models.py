from django.db import models
from apps.users.models import User
# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length = 50)
    description = models.TextField()
    photo = models.ImageField(upload_to = 'videos_image/')
    video = models.FileField(upload_to = 'video_file/')
    date = models.DateTimeField(auto_now_add = True, editable=False)
    user = models.ForeignKey(User, related_name="user_videos", on_delete = models.PROTECT)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"
        
        
class VideoLikes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_like")
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="video_like")
    
class VideoDisLikes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_dislike")
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="video_dislike")
    
class VideoViews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_view")
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="video_view")
    
class VideoComment(models.Model):
    text = models.CharField(max_length= 500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comment")
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="video_comment")
    created = models.DateTimeField(auto_now_add = True)
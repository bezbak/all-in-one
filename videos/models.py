
from tabnanny import verbose
from django.db import models
from users.models import User
# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length = 50)
    description = models.TextField()
    photo = models.ImageField(upload_to = 'videos_image/')
    video = models.FileField(upload_to = 'video_file/')
    views = models.BigIntegerField(default = 0, editable=False)
    likes = models.BigIntegerField(default = 0,editable=False)
    date = models.DateTimeField(auto_now_add = True, editable=False)
    chanel = models.ForeignKey(User,on_delete=models.CASCADE, related_name="chanel")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    profile_image = models.ImageField(upload_to = 'accc/profile/')
    subs = models.PositiveBigIntegerField(default = 0, blank = True, null = True)
    
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользаватель'
        verbose_name_plural = 'Пользаватели'
        
class FollowUser(models.Model):
    from_user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'follower_user' )
    to_user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'following_user')
    
    def __str__(self) -> str:
        return f'{self.to_user} {self.from_user}'
    
    class Meta():
        verbose_name = 'Подписки'
        verbose_name_plural = 'Подписки'
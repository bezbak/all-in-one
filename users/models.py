from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    profile_image = models.ImageField(upload_to = 'accc/profile/')
    
    def __str__(self):
        return self.username

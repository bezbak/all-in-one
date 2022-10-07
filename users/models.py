from tabnanny import verbose
from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    profile_image = models.ImageField(upload_to = 'accc/profile/')
    subs = models.PositiveBigIntegerField(default = 0, blank = True, null = True)
    
    def __str__(self):
        return self.username

from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Setting(models.Model):
    title_site = models.CharField(max_length = 50)
    logo_site = models.ImageField(upload_to = "logo/")
    description_site = models.TextField()
    email_site = models.EmailField()
    instagram_site = models.URLField()
    phone = models.CharField(max_length = 25) 
    
    def __str__(self):
        return self.title_site
    
    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"
        

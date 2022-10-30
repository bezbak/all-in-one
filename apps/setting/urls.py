from django.urls import path
from apps.setting.views import index
urlpatterns = [
    path('', index, name="index"),
    
]
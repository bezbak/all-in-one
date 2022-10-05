from django.shortcuts import render
from .models import Setting
from videos.models import Video
# Create your views here.
def index(request,):
    setting = Setting.objects.latest('id')
    videos = Video.objects.all()
    context = {
        'setting': setting,
        'videos': videos
    }
    return render(request, 'index.html', context)
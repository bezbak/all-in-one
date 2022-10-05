from django.shortcuts import render
from .models import Video
from setting.models import Setting
# Create your views here.

def single_video(request,id):
    video = Video.objects.get(id = id)
    setting = Setting.objects.latest('id')
    context = {
        'setting': setting,
        'video':video
    }
    return render(request, "video.html", context)

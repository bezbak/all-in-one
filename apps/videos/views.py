from django.shortcuts import render, redirect
from apps.videos.models import Video
from apps.setting.models import Setting
# Create your views here.

def single_video(request,id):
    video = Video.objects.get(id = id)
    setting = Setting.objects.latest('id')
    context = {
        'setting': setting,
        'video':video
    }
    return render(request, "video.html", context)

def create_video(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        user = request.user
        title = request.POST.get('title')
        description = request.POST.get('description')
        photo = request.FILES.get('photo')
        video_file = request.FILES.get('video')
        video = Video.objects.create(title = title, description = description, photo =  photo, video = video_file, user = user)
        video.save()
        return redirect('profile', request.user.username)
        
        
    context = {
        'setting':setting
    }
    return render(request,'create_video.html', context)
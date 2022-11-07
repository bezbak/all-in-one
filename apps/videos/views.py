from django.shortcuts import render, redirect
from apps.videos.models import Video, VideoLikes, VideoViews, VideoDisLikes, VideoComment
from apps.setting.models import Setting
from apps.users.models import FollowUser, User
# Create your views here.

def single_video(request,id):
    video = Video.objects.get(id = id)
    setting = Setting.objects.latest('id')
    recomendations = Video.objects.all().order_by('?')
    follow_status = FollowUser.objects.filter(from_user=request.user, to_user=video.user).exists()
    comments = VideoComment.objects.filter(video = video)
    if request.method == 'POST':
        try:
            if 'delete' in request.POST:
                video = Video.objects.get(id = id)
                video.delete()
                return redirect('index')
            if 'like' in request.POST:
                try:
                    like = VideoLikes.objects.get(user = request.user, video =  video)
                    like.delete()
                except:
                    VideoLikes.objects.create(user = request.user, video = video)
            if 'dislike' in request.POST:
                try:
                    dislike = VideoDisLikes.objects.get(user = request.user, video = video)
                    dislike.delete()
                except:
                    VideoDisLikes.objects.create(user = request.user, video = video)
            if 'comment' in request.POST:
                text = request.POST.get('text')
                comment = VideoComment.objects.create(text = text, user = request.user, video = video)
                comment.save()
                return redirect('video', video.id)
            if 'subscribe' in request.POST:
                user = User.objects.get(username=video.user.username)
                try:
                    user = FollowUser.objects.get(from_user = request.user, to_user=video.user)
                    user.delete()
                    user = User.objects.get(username = video.user.username)
                    return redirect('video', video.id)
                except:
                    FollowUser.objects.create(from_user = request.user, to_user = video.user)
                    return redirect('video', video.id)
        except:
            return redirect('index')
    context = {
        'setting': setting,
        'video':video,
        'follow_status': follow_status,
        'comments': comments,
        'recomendations':recomendations
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

    
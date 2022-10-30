from django.shortcuts import render,redirect
from .models import User, FollowUser
from apps.setting.models import Setting
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
# Create your views here.
def register(request):
    setting = Setting.objects.latest("id")
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        profile_image = request.FILES.get('profile_image')
        if password == confirm_password:
            try:
                user = User.objects.create(username = username, email = email,first_name=first_name,last_name =last_name,profile_image=profile_image)
                user.set_password(password)
                user.save()
                user = User.objects.get(username =username )
                user = authenticate(username = username, password = password)
                auth_login(request, user)
                return redirect('index')
            except:
                return redirect('index')
        else:
            return redirect("index")
    context = {
        "setting": setting
    }
    return render(request, 'register.html', context)

def login(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.get(username = username)
        user = authenticate(username = username, password = password)
        auth_login(request, user)
        return redirect('index')
    context = {
        'setting' : setting,
    }
    return render(request, 'login.html', context)

def profile(request, username):
    user = User.objects.get(username = username)
    setting = Setting.objects.latest('id')  
    follow_status = FollowUser.objects.filter(from_user=request.user, to_user=user).exists()
    if request.method == "POST":
        user = User.objects.get(username=username)
        try:
            user = FollowUser.objects.get(from_user = request.user, to_user=user)
            user.delete()
            user = User.objects.get(username = user.username)
            return redirect('profile', user.username)
        except:
            FollowUser.objects.create(from_user = request.user, to_user = user)
            return redirect('profile', user.username)
    context = {
        'user' : user,
        'setting' : setting,
        'follow_status': follow_status
    }
    return render(request, 'account.html', context)

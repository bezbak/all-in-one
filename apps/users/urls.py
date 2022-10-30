from django.urls import path
from apps.users.views import register,login, profile
urlpatterns = [
    path('register/', register, name="register"),
    path('login/', login,name="login"),
    path('profile/<str:username>', profile, name = 'profile'),
]
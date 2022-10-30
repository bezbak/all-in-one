from django.contrib import admin
from .models import User, FollowUser
# Register your models here.
admin.site.register(User)
admin.site.register(FollowUser)
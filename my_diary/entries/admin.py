from django.contrib import admin
from .models import  Entry, Comment
from users.models import Profile
# Register your models here.
admin.site.register(Entry)
admin.site.register(Comment)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "profile_pic", "gender"]
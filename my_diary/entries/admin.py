from django.contrib import admin
from .models import  Entry, Comment
from users.models import Profile, UserFollowing

admin.site.register(UserFollowing)
@admin.register(Entry)
class EntryAdminModel(admin.ModelAdmin):
    list_display = ["owner", "title", "content", "date_created", "date_modified"]


@admin.register(Comment)
class CommentAdminModel(admin.ModelAdmin):
    list_display = ["entry", "text", "date_modified", "date_created"]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "profile_pic", "gender"]

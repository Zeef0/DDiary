from django.contrib import admin
from .models import  Entry, Comment
from users.models import Profile
# Register your models here.

admin.site.register(Comment)

@admin.register(Entry)
class EntryAdminModel(admin.ModelAdmin):
    list_display = ["owner", "title", "date_created", "date_modified", "content"]


@admin.register(Comment)
class CommentAdminModel(admin.ModelAdmin):
    list_display = ["entry", "text", "date_modified", "date_created"]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "profile_pic", "gender"]
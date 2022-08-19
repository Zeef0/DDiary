from django.contrib import admin
from .models import  Entry, Comment
from users.models import Profile
# Register your models here.
admin.site.register(Entry)
admin.site.register(Comment)
admin.site.register(Profile)
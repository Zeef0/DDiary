from django.urls import path
from django.contrib.auth import views as auth_views
from .import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("create/profile", views.CreateUserView.as_view(), name="create_user"),
    path("<str:slug>/", views.UserProfileView.as_view(), name="users_profile")

]
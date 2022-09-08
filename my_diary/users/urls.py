from django.urls import path
from .import views
app_name = "users"
urlpatterns = [
    path("register/", views.CreateUserView.as_view(), name="create_user"),
    path("<str:slug>/", views.UserProfileView.as_view(), name="users_profile")

]
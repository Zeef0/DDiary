from django.urls import path
from .import views
app_name = "users"
urlpatterns = [
    path("register/", views.CreateUserView.as_view(), name="create_user"),
    path("<slug:slug>/", views.UserProfileView.as_view(), name="users_profile"),
    path("<slug:slug>/update", views.UpdateProfileView.as_view(), name="update_profile"),
    path("<slug:slug>/update/user", views.UpdateUserView.as_view(), name="update_user")

]
#r'^profile/username/(?P<slug>[\w.@+-]+)/$'
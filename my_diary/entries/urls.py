from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("new/entry", views.CreateEntryView.as_view(), name="create_entry")
]
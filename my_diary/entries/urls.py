from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("entry/<slug:slug>", views.EntryDetailView.as_view(), name="entry_detail"),
    path("new/entry", views.CreateEntryView.as_view(), name="create_entry")
]
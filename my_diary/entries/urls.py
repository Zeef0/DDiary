from django.urls import path, include
from . import views

app_name = "entries"
urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("entry/<slug:slug>", views.EntryDetailView.as_view(), name="entry_detail"),
    path("new/entry", views.CreateEntryView.as_view(), name="create_entry"),
    path("entry/filter_by/<slug:slug>", views.FilteredPostTag.as_view(), name="filtered_post"),
    path("update/entry/<slug:slug>", views.UpdateEntryView.as_view(), name="update_entry"),
    path("delete/entry/<int:pk>", views.EntryDeleteView.as_view(), name="delete_entry"),

    # Comment related Crud
    path("entry/<slug:slug>/add/comment", views.postcomment, name="create_comment"),
    path("delete/comment/<int:pk>", views.DeleteCommentView.as_view(), name="delete_comment")


]
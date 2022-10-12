from django.shortcuts import render, get_list_or_404, get_object_or_404, reverse, redirect
from django.urls import reverse_lazy
from django.db.models import Q, F, Count
from .models import Entry, Comment
from django.contrib.auth.models import User 


from django.contrib.auth.decorators import login_required


from django.views.generic import (
    ListView,
    DetailView
    )
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import EntryForm, CommentForm
from users.models import Profile

from django.core.mail import send_mail 
from pprint import pprint
from decouple import config
from taggit.models import Tag

class Home(ListView):
    model = Entry
    template_name = "entries/home.html"
    context_object_name = "context"


    
    def get_queryset(self):

        """
        Get query if user search something
        """
        search = self.kwargs.get("search")
        qs = ""
        if search:
            qs = Entry.objects.filter(Q(owner__icontains=search)| Q(tags=search)|Q(content__icontains=search))
        qs = Entry.objects.filter(Q(privacy="Public")| Q(owner__id= self.request.user.pk)).order_by("-view_count")
        
        return qs
 



class FilteredPostTag(ListView):
    model = Entry
    template_name = "entries/filter_by_tag.html"
    context_object_name = "context"

    def get_queryset(self, *args, **kwargs):
        """
            Get the related entries through slug
        """
        object_list = Entry.objects.all()
        tag_obj = get_object_or_404(Tag, slug=self.kwargs["slug"])
        qs = object_list.filter(tags__in=[tag_obj])
        return qs

class EntryDetailView(DetailView):
    model = Entry
    context_object_name = "content"

    def get_object(self, queryset=None):
        """
        Get the current instance of the model through slug then increment 
        view count by one
        """
        item = super().get_object(queryset)
        item.increment_view_count()
        return item



class CreateEntryView(LoginRequiredMixin, CreateView):
    model = Entry
    form_class = EntryForm
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)



class UpdateEntryView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Entry
    fields = ["title", "privacy", "content", "images"]


    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user.id == post.owner.id:
            return True
        return False


class EntryDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView): 
    model = Entry
    success_url = reverse_lazy("entries:home")


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.owner: # test this chek if wrong 
            return True
        return False


@login_required
def postcomment(request, slug):
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            entry = get_object_or_404(Entry, slug=slug)
            form.instance.entry = entry
            form.save()
            return redirect("entries:home")
    return render(request, "entries/create_comment.html", {"form": form, "post": Entry.objects.get(slug=slug)})

class DeleteCommentView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Comment
    success_url = reverse_lazy("entries:home")

    def test_func(self):
        obj = self.get_object()
        if self.request.user == obj.entry.owner:
            return True
        return False

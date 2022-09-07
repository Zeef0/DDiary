from django.shortcuts import render, get_list_or_404, get_object_or_404, reverse, redirect
from django.urls import reverse_lazy
from django.db.models import Q, F, Count
from .models import Entry, Comment


from django.contrib.auth.decorators import login_required


from django.views.generic import (
    ListView,
    DetailView
    )
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import EntryForm, CommentForm
from users.models import Profile


from pprint import pprint

class Home(ListView):
    model = Entry
    template_name = "entries/home.html"
    context_object_name = "context"
    
    def get_queryset(self):

        """
        Show all items where entries are set to public 
        """
        qs = Entry.objects.filter(Q(privacy="Public")| Q(owner__pk= self.request.user.pk)).order_by("-view_count")
        pprint(dir(qs), indent=2)
        
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
    success_url = reverse_lazy("entries:home")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)



class UpdateEntryView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Entry
    fields = ["title", "privacy", "content"]


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
    return render(request, "entries/create_comment.html", {"form": form})

class DeleteCommentView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Comment
    success_url = reverse_lazy("entries:home")

    def test_func(self):
        obj = self.get_object()
        if self.request.user == obj.entry.owner:
            return True
        return False

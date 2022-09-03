from django.shortcuts import render, get_list_or_404, get_object_or_404, reverse
from django.db.models import Q, F
from .models import Entry, Comment

from django.views.generic import (
    ListView,
    DetailView
    )
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import EntryForm
from users.models import Profile


class Home(ListView):
    model = Entry
    template_name = "entries/home.html"
    context_object_name = "context"
    
    def get_queryset(self):

        """
        Show all items where entries are set to public 
        """
        qs = Entry.objects.filter(Q(privacy="Public")| Q(owner__pk= self.request.user.pk))
        
        return qs


class EntryDetailView(DetailView):
    model = Entry
    context_object_name = "content"
    



class CreateEntryView(LoginRequiredMixin, CreateView):
    model = Entry
    form_class = EntryForm
    success_url = "/"

    def form_valid(self, form):
        form.instance.owner = Profile.objects.get(user=self.request.user)
        return super().form_valid(form)



class UpdateEntryView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Entry
    fields = ["title", "privacy", "content"]


    def form_valid(self, form):
        form.instance.owner = self.request.owner
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user.id == post.owner.id:
            return True
        return False


class EntryDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView): 
    model = Entry
    success_url = "/"
    def test_func(self):
        post = self.get_object()
        if self.request.user.id == post.owner.id:
            return True
        return False

    # def get_object(self, queryset=None):
    #     pk = self.request.POST("pk")
    #     return self.get_queryset().filter(pk=pk).get()
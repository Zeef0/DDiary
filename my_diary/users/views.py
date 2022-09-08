from django.shortcuts import render
from .models import Profile
from django.contrib.auth.models import User
from entries.models import Entry, Comment
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import (
    ListView,
    DetailView
    )
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import UserCreationForm 


class CreateUserView(CreateView):
    model = User
    form_class  = UserCreationForm

    template_name = "users/create_profile.html"
    success_url = reverse_lazy("entries:home")


class UserProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = "users/users_profile.html"
    context_object_name = "profile"
    slug_field = "user__username"

class UpdateProfileView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ["profile_pic", "gender", "bio"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    
    def test_func(self):
        item = self.get_obj()
        if item.user == self.request.user:
            return True
        return False

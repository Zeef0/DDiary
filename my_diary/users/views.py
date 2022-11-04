from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Profile, UserFollowing
from entries.models import Entry, Comment
from django.urls import reverse_lazy


from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView


from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import UserRegistrationForm

from decouple import config

from my_diary.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from smtplib import SMTPException
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class CreateUserView(CreateView):
    model = User
    form_class  = UserRegistrationForm

    template_name = "users/create_profile.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        html_message = render_to_string("entries/user_creation.html")
        message = strip_tags(html_message)
        send_mail(
            f"Account Created for {username}",
            message,
            config("EMAIL_HOST_USER"),
            (email, ),
        html_message
        )
        return super().form_valid(form)

class UserProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = "users/users_profile.html"
    context_object_name = "profile"
    slug_field = "user__username"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(username=self.kwargs.get("slug"))
        context["all_post"] = Entry.objects.all().filter(owner=user)
        context["count"] = UserFollowing.objects.all().filter(user_id=user).count()
        context["followers"] = UserFollowing.objects.all().filter(user_id=user)
        print(context)
        return context

class UpdateProfileView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ["profile_pic", "gender", "location", "bio"]
    slug_field = "user__username"
    success_url = reverse_lazy("entries:home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    
    def test_func(self):
        item = self.get_object()
        if item.user == self.request.user:
            return True
        return False


class UpdateUserView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = User
    slug_field = "username"
    fields = ["username", "email"]
    success_url = reverse_lazy("entries:home")
    template_name = "users/user_update_form.html"
    def form_valid(self, form):
        form.user = self.request.user
        return super().form_valid(form)

    
    def test_func(self):
        item = self.get_object()
        if item.username== self.request.user.username:
            return True
        return False


def follow_user(request, username):
    user_following = get_object_or_404(User, username=username)
    UserFollowing.objects.create(user_id=request.user, following_user_id=user_following)
    return redirect("entries:home")
from .models import Profile
from django.contrib.auth.models import User
from entries.models import Entry, Comment
from django.urls import reverse_lazy


from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import (ListView, DetailView )


from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import UserCreationForm 

from decouple import config

from my_diary.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from smtplib import SMTPException
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class CreateUserView(CreateView):
    model = User
    form_class  = UserCreationForm

    template_name = "users/create_profile.html"
    success_url = reverse_lazy("entries:home")

    def form_valid(self, form):

        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        print(form.cleaned_data)
        email = form.cleaned_data.get("email")
        html_message = render_to_string("entries/user_creation.html")
        message = strip_tags(html_message)
        send_mail(
            f"Account Created for {username}",
            message,
            config("EMAIL_HOST_USER"),
        ( "jhayjane78@gmail.com", ),
        html_message
        )
        return super().form_valid(form)

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

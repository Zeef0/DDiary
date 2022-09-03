from django.shortcuts import render
from .models import Profile
from django.views.generic import (
    ListView,
    DetailView
    )
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from entries.models import Entry, Comment



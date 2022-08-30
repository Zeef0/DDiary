from django.shortcuts import render, get_list_or_404, get_object_or_404

from .models import Entry, Comment

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import EntryForm
from users.models import Profile


class Home(ListView):
    model = Entry
    template_name = "entries/home.html"
    context_object_name = "context"


    def get_queryset(self):
        qs = Entry.objects.all().filter(privacy="Public")
        return qs


class CreateEntryView(LoginRequiredMixin, CreateView):
    model = Entry
    form_class = EntryForm
    success_url = "/"

    def form_valid(self, form):
        form.instance.owner = Profile.objects.get(user=self.request.user)
        return super().form_valid(form)

def update_entry_view(request, pk):
    data = get_object_or_404(pk=pk)
    if data.pk == request.user.pk:
        form = "form"


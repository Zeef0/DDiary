from django.shortcuts import render, get_list_or_404
from .models import Entry, Comment

def home(request):
    diaries = get_list_or_404(Entry)
    return render(request, "entries/home.html", {"context": diaries})
from .models import  Entry

from django import forms

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        exclude = ["owner", "date_created", "date_modified"]
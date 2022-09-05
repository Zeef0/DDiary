from .models import  Entry, Comment

from django import forms

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        exclude = ["owner","date_created", "date_modified"]


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude =  ["entry"]

        widgets = {
            "text": forms.TextInput(attrs={"class": "form-control"})
        }
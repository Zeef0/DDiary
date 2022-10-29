from .models import  Entry, Comment

from django import forms

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ["title", "tags", "privacy", "content", "images"]

        widgets = {
            "images": forms.ClearableFileInput(attrs={"class": "btn-success", "class": "btn"})
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude =  ["entry"]

        widgets = {
            "text": forms.TextInput(attrs={"class": "form-control"})
        }
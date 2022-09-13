from .models import  Entry, Comment

from django import forms

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        exclude = ["owner","date_created", "date_modified", "slug", "view_count"]


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude =  ["entry"]

        widgets = {
            "text": forms.TextInput(attrs={"class": "form-control"})
        }
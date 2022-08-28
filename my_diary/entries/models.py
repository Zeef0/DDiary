from django.db import models
from users.models import Profile

from ckeditor.fields import RichTextField
from django.dispatch import receiver

class Entry(models.Model):
    VISIBILITY = (
        ("TO Anyone", "Public"),
        ("None", "Private")
    )
    privacy = models.CharField(max_length=13, help_text="Who can see this diary?", default="Public")
    title = models.CharField(max_length=80)
    content = RichTextField()
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    images = models.ImageField(blank=True, upload_to="users/images")


    class Meta:
        verbose_name_plural = "entries"
        ordering = ["-date_created"]

    def __str__(self):
        return self.title

class Comment(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name="entries")
    text = models.CharField(max_length=120)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date_modified"]

    def __str__(self):
        return self.title[0] + self.title[1:10]
# @receiver(post_delete, sender=Entry)
# def diary_pictures_delete(sender, instance, **kwargs):
#     instance.image.delete(False)
from django.db import models
from django.contrib.auth.models import User
from users.models import Profile

from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from django.dispatch import receiver

from django.utils.text import slugify 

class Entry(models.Model):
    VISIBILITY = (
        ("TO Anyone", "Public"),
        ("None", "Private")
    )
    title = models.CharField(max_length=80)
    privacy = models.CharField(max_length=13, help_text="Who can see this diary?", default="Public")
    content = RichTextField()
    images = models.ImageField(blank=True, upload_to="users/images")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True)
    view_count = models.IntegerField(default=0)
    tags = TaggableManager()


    def increment_view_count(self):
        self.view_count += 1
        self.save()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Entry, self).save(*args, **kwargs)


    class Meta:
        verbose_name_plural = "entries"
        ordering = ["-date_created"]

    def __str__(self):
        return self.title

class Comment(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name="all_comments")
    text = models.CharField(max_length=120)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date_modified"]

    def __str__(self):
        return self.text

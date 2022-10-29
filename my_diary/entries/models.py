from django.db import models
from django.contrib.auth.models import User
from users.models import Profile

from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from django.dispatch import receiver

from django.utils.text import slugify 
from django.urls import reverse 


def upload_to_directory(instance, filename):
    return f"user_{instance.owner.username}/filename"

    
class Entry(models.Model):
    VISIBILITY = (
        ("TO Anyone", "Public"),
        ("None", "Private")
    )


    content = RichTextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    images = models.ImageField(blank=True, upload_to=upload_to_directory)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    privacy = models.CharField(max_length=13, help_text="Who can see this diary?", default="Public")
    slug = models.SlugField(blank=True)
    tags = TaggableManager(blank=True)
    title = models.CharField(max_length=80, blank=True)
    view_count = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Entry"
        verbose_name_plural = "entries"
        ordering = ["-date_created"]
        
    def increment_view_count(self):
        self.view_count += 1
        self.save()

    def get_absolute_url(self):
        return reverse("entries:entry_detail", kwargs={"slug": self.slug })

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Entry, self).save(*args, **kwargs)



    def __str__(self):
        return self.title

class Comment(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name="comments")
    text = models.CharField(max_length=120, help_text="Add a comment")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date_modified"]
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        # db_table = "entry_comment"

    def __str__(self):
        return self.text

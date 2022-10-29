from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Entry, Comment 

@receiver(post_save, Entry)
def create_slug(instance, slug, **kwargs):
    pass
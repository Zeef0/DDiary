from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Non-binary", "Non-binary"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default="profile_pic.jpeg", upload_to="profile_pic")
    gender = models.CharField(max_length=10, blank=True, choices=GENDER_CHOICES)

    def __str__(self):
        return self.user.username


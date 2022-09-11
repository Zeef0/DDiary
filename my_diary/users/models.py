from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Non-binary", "Non-binary"),
    )
    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default="profile_pic.jpeg", upload_to="profile_pic")
    gender = models.CharField(max_length=10, blank=True, choices=GENDER_CHOICES)
    bio = models.CharField(max_length=120, blank=True)


    def __str__(self):
        return self.user.username



# class UserFollowing(models.Model):
class UserFollowing(models.Model):
    user_id = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)


    following_user_id = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE)

    # You can even add info about when user started following
    created = models.DateTimeField(auto_now_add=True)
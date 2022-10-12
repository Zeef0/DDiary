from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Non-binary", "Non-binary"),
    )
    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default="default_profile.png", upload_to="profile_pic")
    gender = models.CharField(max_length=10, blank=True, choices=GENDER_CHOICES)
    bio = models.CharField(max_length=120, blank=True)

    class Meta:
        get_latest_by = "user"
        db_table = "users_profile"
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.profile_pic.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)

    def get_absolute_url(self):
        return reverse("users:users_profile", kwargs=self.kwargs.get("slug"))



class UserFollowing(models.Model):

    """
        Follow functionality to user model
    """
    user_id = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)


    following_user_id = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE)

    
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
            You can't follow the same person twice 
        """
        unique_together = ["user_id", "following_user_id"]
    
    def __str__(self):
        return "{} followed user {}".format(self.user_id.username, self.following_user_id.username)




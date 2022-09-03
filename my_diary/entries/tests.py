from django.test import TestCase
from django.contrib.auth.models import User
from user.models import Profile

# Create your tests here.
# class UserProfileTestCase(TestCase):
#     def setup(self):
#         User.objects.create_user("Jhay", "lennon@thebeatles.com", "jhayzero")
#         User.objects.create_user("Jha22y", "lennon@the22beatles.com", "jhay2zero")

#         def test_check_profile_and_user(self):
#             jhay1 = User.objects.get(id=1)
#             profile_jhay = Profile.objects.filter(id=1)

#             self.AssertEqual(jhay1.username, profile_jhay.user)

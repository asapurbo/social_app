from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# signup info
class SignUp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='signup')
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    profile_pic = models.TextField(max_length=200, null=True, blank=True)
    bg_pic = models.TextField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    isValid = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

# extra info
class ExtraInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='extra_info')
    bio = models.TextField(null=True, blank=True)
    posts = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

class Device(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='device')
    device_name = models.CharField(max_length=255, blank=True, null=True)
    device_type = models.CharField(max_length=255, blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    model_number = models.CharField(max_length=255, blank=True, null=True)
    serial_number = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_logged_in = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.device_name


# Follow
class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follow_models_user')
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


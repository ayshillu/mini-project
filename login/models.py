from django.db import models
from django.contrib.auth.models import AbstractUser, User

class EditProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    job = models.CharField(max_length=15, null=True)
    location = models.CharField(max_length=10, null=True)
    Yearofexp = models.IntegerField(null=True)
    profile_pic = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    # date_created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'Edit Profile'
        verbose_name_plural = 'Edit Profiles'  

class EditProfileClient(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    Phoneno= models.IntegerField(null=True)
    location = models.CharField(max_length=10, null=True)
    # profile_pic = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    # date_created = models.DateTimeField(auto_now_add=True, null=True)       

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

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

class RatingComment(models.Model):
    RATING_CHOICES = (
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    )

    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Rating: {self.rating}, Comment: {self.comment}"

class ReviewRating(models.Model):
    photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

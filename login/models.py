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

    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='sent_rating')
    to_user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='received_recieved')
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Rating: {self.rating}, Comment: {self.comment}"

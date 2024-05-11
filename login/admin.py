from django.contrib import admin
from .models import EditProfile, EditProfileClient, RatingComment

admin.site.register(EditProfile)
admin.site.register(EditProfileClient)
admin.site.register(RatingComment)
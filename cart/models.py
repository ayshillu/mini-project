from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=20, null=True)
    desc = models.CharField(max_length=100, null=True)
    price = models.IntegerField(null=True)
    image = models.ImageField(upload_to="product_images/", null=True, blank=True, default='')
    quatity = models.IntegerField(null=True)

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Products, through='CartItem')

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

class PaymentDetails(models.Model):
    email = models.EmailField()
    card_number = models.CharField(max_length=16)
    card_expiry = models.CharField(max_length=7)  # MM/YYYY format
    cardholder_name = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    district = models.CharField(max_length=100)



class Notifications(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
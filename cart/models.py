from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=20, null=True)
    desc = models.CharField(max_length=100, null=True)
    price = models.IntegerField(null=True)
    image_field = models.CharField(max_length=1000, null=True)
    quatity = models.IntegerField(null=True)

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Products, through='CartItem')

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
from django.contrib import admin
from .models import Products
from .models import Cart
from .models import CartItem,PaymentDetails, Notifications

admin.site.register(Products)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(PaymentDetails)
admin.site.register(Notifications)
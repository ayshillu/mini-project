from django.urls import path
from .views import  add_to_cart, cart

urlpatterns = [
    # path('shop/', shop, name='shop'),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
    path('cart/', cart, name='cart'),
    # Other URL patterns...
]

from django.urls import path
from .views import shop, add_to_cart

urlpatterns = [
    path('shop/', shop, name='shop'),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
    # Other URL patterns...
]

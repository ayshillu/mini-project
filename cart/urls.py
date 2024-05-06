from django.urls import path
from .views import  add_to_cart, cart, add_product, loss_product, checkout, payment_details
from django.conf import settings
from django.conf.urls.static import static
from .views import delete_item,sell_product

urlpatterns = [
    # path('shop/', shop, name='shop'),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
    path('cart/', cart, name='cart'),
    path('add_product', add_product, name="add_product" ),
    path('loss_product', loss_product, name="loss_product" ),  # Add a comma here
    path('checkout', checkout, name="checkout" ),
    path('payment_details/', payment_details, name="payment_details" ),
    path('delete_item', delete_item, name='delete_item'),
    path('sell_product/', sell_product, name='sell_product'),
    # Other URL patterns...
]

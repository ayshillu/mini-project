from django.shortcuts import render, redirect
from .models import Products, Cart, CartItem

def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = Products.objects.get(pk=product_id)
        user = request.user
        # Check if the user has a cart
        if hasattr(user, 'cart'):
            cart = user.cart
        else:
            # If user does not have a cart, create one
            cart = Cart.objects.create(user=user)
        # Check if the product is already in the cart
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        # If the product is already in the cart, increase the quantity
        if not created:
            cart_item.quantity += 1
            cart_item.save()

    return redirect('cart')

# def shop(request):
#     products = Products.objects.all()
#     context = {
#         'products': products
#     }
#     return render(request, 'shop.html', context)

def cart(request):
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = user_cart.cartitem_set.all()
    subtotal = sum(item.product.price * item.quantity for item in cart_items)
    total_price = subtotal + 5  # Assuming a fixed shipping cost of €5
    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'total_price': total_price,
    }
    return render(request, 'cart.html', context)

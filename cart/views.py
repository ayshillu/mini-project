from django.shortcuts import render, redirect
from .models import Products, Cart, CartItem
from django.shortcuts import get_object_or_404
from .models import PaymentDetails ,User
from .models import CartItem


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

def add_product(request):
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Products, pk=product_id)
        # Check if the product already exists in the user's cart
        cart_item, created = CartItem.objects.get_or_create(cart=user_cart, product=product)
        if not created:
            # If the product already exists, increment its quantity
            cart_item.quantity += 1
            cart_item.save()
    
    return redirect("cart")

# def loss_product(request):
#     user_cart, created = Cart.objects.get_or_create(user=request.user)
#     if request.method == 'POST':
#         product_id = request.POST.get('product_id')
#         product = get_object_or_404(Products, pk=product_id)
#         # Check if the product already exists in the user's cart
#         cart_item, created = CartItem.objects.get_or_create(cart=user_cart, product=product)
#         if not created:
#             # If the product already exists, increment its quantity
#             cart_item.quantity -= 1
#             cart_item.save()
    
#     return redirect("cart")

def loss_product(request):
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Products, pk=product_id)
        # Check if the product already exists in the user's cart
        cart_item, created = CartItem.objects.get_or_create(cart=user_cart, product=product)
        if not created:
            # If the product already exists, decrement its quantity
            if cart_item.quantity > 0:
                cart_item.quantity -= 1
                cart_item.save()
            # If the quantity becomes 0, redirect to delete_item view
            if cart_item.quantity == 0:
                CartItem.objects.filter(product_id=product_id).delete()
        # Redirect to the cart page or any other page as needed
    return redirect("cart")

def passprice(request):
        user_cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = user_cart.cartitem_set.all()
        subtotal = sum(item.product.price * item.quantity for item in cart_items)
        total_price = subtotal + 5  # Assuming a fixed shipping cost of €5
        context = {
            'cart_items': cart_items,
            'subtotal': subtotal,
            'total_price': total_price,  # Include total_price in the context
        }
        return render(request, 'checkout.html', context)

def payment_details(request):
    if request.method == 'POST':
        # Handle form submission
        email = request.POST.get('email')
        card_number = request.POST.get('card_number')
        card_expiry = request.POST.get('card_expiry')
        cardholder_name = request.POST.get('cardholder_name')
        zip_code = request.POST.get('zip_code')
        district = request.POST.get('district')
        
        # Create a PaymentDetails object
        payment_details = PaymentDetails.objects.create(
        email=email,
        card_number=card_number,
        card_expiry=card_expiry,
        cardholder_name=cardholder_name,
        zip_code=zip_code,
        district=district)

        payment_details.save()
        
        # Perform any additional operations like calculating total price, etc.
        
        # Redirect to a success page or display a success message
    return render(request, 'thankyou.html')

def thankyou(request):
       
    me = request.user

    context = {
        'user' : User,
        'me': me,

    }
    return render(request, 'thankyou.html', context)

def delete_item(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        # Assuming you have a CartItem model
        CartItem.objects.filter(product_id=product_id).delete()
        # Redirect to the cart page or any other page as needed
        return redirect('cart')  # Replace 'cart_page' with your actual URL name    


def sell_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES.get('image')

        product = Products()  # Instantiate a new Products object
        product.name = name
        product.desc = description
        product.price = price
        if image:
            product.image = image
        product.save()

        return redirect('shop')  # Redirect to the shop page after adding the product

    return render(request, 'sellproduct.html')

def checkout(request):
    if request.method == 'POST':
        pay_and_clear_cart = request.POST.get('pay_and_clear_cart')
        if pay_and_clear_cart == 'true':
            # Clear all cart items
            CartItem.objects.all().delete()
            # Redirect to the thank you page or any other page as needed
            return redirect('thankyou')
    return render(request, 'checkout.html')


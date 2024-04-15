from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import EditProfile
from cart.models import Products, Cart, CartItem

# Create your views here.

def signup(request):

    if request.method == "POST":
      username = request.POST['username']
      fname = request.POST['fname']
      lname = request.POST['lname']
      email = request.POST['email']
      pass1 = request.POST['pass1']
    
      myuser = User.objects.create_user(username, email, pass1)
      myuser.first_name = fname
      myuser.last_name = lname

      myuser.save()

      messages.success(request, "Your Account has been successfully created. ")

      return redirect('signin')
    
    
    
    
    return render(request, 'signup.html', {'user': request.user})

def signin(request):

    

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request,"homelogout.html", {'fname': fname})
        
        else:
            messages.error(request, "Bad Credential")
            return redirect('home')

    return render(request, 'signin.html')


def home(request):
    return render(request, 'home.html')

def signout(request):
    pass

def about(request):
    return render(request, 'about.html')

def profile(request):
    me = request.user
    try:
        profile = EditProfile.objects.get(user=request.user)
    except:
        profile = EditProfile(user=request.user)

    context = {
        'user' : User,
        'me': me,
        'profile' : profile,

    }
    return render(request, 'profile.html', context)

def blog(request):
    return render(request, 'blog.html')

def services(request):
    profiles = EditProfile.objects.all()
    # for i in profiles:
    #     print(i.user)

    context = {
        'profiles': profiles,
    }

    return render(request, 'services.html' , context)


def contact(request):
    return render(request, 'contact.html')

@login_required
def editprofile(request):
    try:
        profile = EditProfile.objects.get(user=request.user)
    except:
        profile = EditProfile(user=request.user)

    context={
        'profile':profile,
    }

    if request.method == 'POST':
        job = request.POST['job']
        location = request.POST['location']
        year = request.POST['year']

        # print(job,location,year)
        try:
            profile = EditProfile.objects.get(user=request.user)
        except:
            profile = EditProfile(user=request.user)

        profile.job = job
        profile.location = location
        profile.Yearofexp = year

        profile.save()


        return HttpResponseRedirect(reverse("profile"))
   
    return render(request, 'editprofile.html', context)
 
 
def chatprofile(request):
      return render(request, 'chatprofile.html')

def shop(request):
    products = Products.objects.all()

    context = {
        'products' : products
    }
    return render(request, 'shop.html', context)

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


def cart(request):
      return render(request, 'cart.html')

def thankyoupage(request):
      return render(request, 'thankyoupage.html')

def checkout(request):
      return render(request, 'checkout.html')

def thankyou(request):
       
    me = request.user

    context = {
        'user' : User,
        'me': me,

    }
    return render(request, 'thankyou.html', context)

def homelogout(request):
      return render(request, 'homelogout.html')
      


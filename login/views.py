from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
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
        pass1 = request.POST['password']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            if not user.is_superuser:
                messages.error(request, "Bad credential")
                fname = user.first_name
                return render(request,"homelogout.html", {'fname': fname})
            else:
                messages.error(request, "Bad credentials")
                return redirect('signin')
        
        else:
            messages.error(request, "Bad Credential")
            return redirect('signin')

    return render(request, 'signin.html')


def home(request):
    return render(request, 'home.html')

def signout(request):
    pass

def about(request):
    return render(request, 'about.html')

def appointment(request):
    return render(request, 'appointment.html')

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



# def cart(request):
#       return render(request, 'cart.html')

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
      logout(request)
      messages.success(request, "Logout successfull")
      return redirect('signin')
      


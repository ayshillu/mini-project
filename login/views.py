from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import EditProfile, EditProfileClient
from cart.models import Products
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from cart.models import Notifications




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
                return render(request,"dash.html", {'fname': fname})
            else:
                messages.error(request, "Bad credentials")
                return redirect('signin')
        
        else:
            messages.error(request, "Bad Credential")
            return redirect('signin')

    return render(request, 'signin.html')


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def homeclient(request):
    return render(request, 'homeclient.html')



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

def clientprofile(request):
    me = request.user
    try:
        profile = EditProfileClient.objects.get(user=request.user)
    except:
        profile = EditProfileClient(user=request.user)

    context = {
        'user' : User,
        'me': me,
        'profile' : profile,

    }
    return render(request, 'clientprofile.html', context)

def blog(request):
    return render(request, 'blog.html')

def services(request):
    profiles = EditProfile.objects.all()

    context = {
        'profiles': profiles,
    }

    return render(request, 'services.html' , context)

def clientservice(request):
    profiles = EditProfileClient.objects.all()

    context = {
        'profiles': profiles,
    }

    return render(request, 'client_service.html' , context)

def contact(request):
    return render(request, 'contact.html')

@login_required
def editprofile(request):
    try:
        profile = EditProfile.objects.get(user=request.user)
    except EditProfile.DoesNotExist:
        profile = EditProfile(user=request.user)

    context = {
        'profile': profile,
    }

    if request.method == 'POST':
        job = request.POST.get('job')
        location = request.POST.get('location')
        year = request.POST.get('year')
        photo = request.FILES.get('photo')

        if photo:
            fs = FileSystemStorage()  # Use default storage
            filename = fs.save(photo.name, photo)
            profile.profile_pic = filename  # Save only the filename, not full path

        profile.job = job
        profile.location = location
        profile.Yearofexp = year
        profile.save()

        return HttpResponseRedirect(reverse("profile"))
   
    return render(request, 'editprofile.html', context)

def clienteditprofile(request):
    try:
        profile = EditProfileClient.objects.get(user=request.user)
    except EditProfileClient.DoesNotExist:
        profile = EditProfileClient(user=request.user)

    if request.method == 'POST':
        phoneno = request.POST.get('phoneno')
        location = request.POST.get('location')

        try:
            profile = EditProfileClient.objects.get(user=request.user)
        except EditProfileClient.DoesNotExist:
            profile = EditProfileClient(user=request.user)

        profile.Phoneno = phoneno
        profile.location = location
        profile.save()

        return HttpResponseRedirect(reverse("clientprofile"))
   
    context = {
        'profile': profile,
    }
   
    return render(request, 'editp_client.html', context)


 
 
def chatprofile(request):
      return render(request, 'chatprofile.html')

def shop(request):
    products = Products.objects.all()
    # Fetch notifications count for the current user
    notification_count = Notifications.objects.filter(user=request.user).count()

    context = {
        'products' : products,
        'notification_count' : notification_count,
    }
    return render(request, 'shop.html', context)

def clientshop(request):
    products = Products.objects.all()

    context = {
        'products' : products
    }
    return render(request, 'client_shop.html', context)



# def cart(request):
#       return render(request, 'cart.html')

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

def gotohome(request):
    return render(request, 'homelogout.html')
      
def henna(request):
    
    profiles = EditProfile.objects.all()

    context = {
        'profiles': profiles,
    }

    return render(request, 'henna.html', context)

def homenurse(request):
    profiles = EditProfile.objects.all()

    context = {
        'profiles': profiles,
    }

    return render(request, 'homenurse.html' , context)

def tailor(request):
    profiles = EditProfile.objects.all()

    context = {
        'profiles': profiles,
    }

    return render(request, 'tailor.html', context)

def maid(request):
    profiles = EditProfile.objects.all()

    context = {
        'profiles': profiles,
    }

    return render(request, 'maid.html', context)

def apphenna(request):
    return render(request, 'apphenna.html')

def appnurse(request):
    return render(request, 'appnurse.html')

def appmaid(request):
    return render(request, 'appmaid.html')

def apptailor(request):
    return render(request, 'apptailor.html')

def dash(request):
    return render(request, 'dash.html')


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
from .models import  UserProfile

# Create your views here.


def index(request):
    return render(request, 'login.html')

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
            return render(request,"workers.html", {'fname': fname})
        
        else:
            messages.error(request, "Bad Credential")
            return redirect('workers')

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

    # print(profile)

    context = {
        'user' : User,
        'me': me,
        'profile' : profile,

    }
    return render(request, 'profile.html', context)

def blog(request):
    return render(request, 'blog.html')

def workers(request):
    return render(request, 'workers.html')


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

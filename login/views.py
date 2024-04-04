from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


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
            return render(request,"login.html", {'fname': fname})
        
        else:
            messages.error(request, "Bad Credential")
            return redirect('login')

    return render(request, 'signin.html')


def home(request):
    return render(request, 'home.html')

def signout(request):
    pass

def about(request):
    return render(request, 'about.html')

def profile(request):
    return render(request, 'profile.html')

def blog(request):
    return render(request, 'blog.html')

def workers(request):
    return render(request, 'workers.html')


def contact(request):
    return render(request, 'contact.html')

def selman(request):
    return render(request, 'selman.html')


def submit(request):
    # view to load all recievers detail page
    user_name=request.user
    count = 1

    context = {
        'user' : user_name,
    }

    return render(request, 'profile.html', context)
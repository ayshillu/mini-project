from django.contrib import admin
from django.urls import path, include
from login import views

# Define urlpatterns
urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('home', views.home, name="home"),
    path('about', views.about , name="about"),
    path('profile', views.profile , name="profile"),
    path('blog', views.blog , name="blog"),
    path('services', views.services , name="services"),
    path('contact', views.contact , name="contact"),
    path('editprofile', views.editprofile, name='editprofile'),
    path('chatprofile', views.chatprofile , name="chatprofile"),
    path('shop', views.shop , name="shop"),
    # path('cart', views.cart , name="cart"),
    path('thankyou', views.thankyou , name="thankyou"),
    path('checkout', views.checkout , name="checkout"),
    path('homelogout', views.homelogout , name="homelogout"),
    path('appointment', views.appointment , name="appointment"),
    
]


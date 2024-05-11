from django.contrib import admin
from django.urls import path, include
from login import views

# Define urlpatterns
urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
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
    # path('checkout', views.checkout , name="checkout"),
    path('homelogout', views.homelogout , name="homelogout"),
    path('apphenna', views.apphenna , name="apphenna"),
    path('appnurse', views.appnurse , name="appnurse"),
    path('appmaid', views.appmaid , name="appmaid"),
    path('apptailor', views.apptailor , name="apptailor"),
    path('gotohome', views.gotohome , name="gotohome"),
    path('henna', views.henna , name="henna"),
    path('homenurse', views.homenurse , name="homenurse"),
    path('tailor', views.tailor , name="tailor"),
    path('maid', views.maid , name="maid"),
    path('maid', views.maid , name="maid"),
    path('dash', views.dash , name="dash"),
    path('homeclient', views.homeclient , name="homeclient"),
    path('clientservice', views.clientservice , name="clientservice"),
    path('clienteditprofile', views.clienteditprofile, name='clienteditprofile'),
    path('clientshop', views.clientshop , name="clientshop"),
    path('clientprofile', views.clientprofile , name="clientprofile"),
    path('rate_and_comment', views.rate_and_comment , name="rate_and_comment"),
  
    
]


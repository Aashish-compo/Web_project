from django.contrib import admin
from django.urls import path, include
from myapp.views import signup, login, index, contact,about

urlpatterns = [

    path("about" , about, name = "about"),
    path("index", index, name="home"),
    path("signup", signup, name="signup"),
    path("", login, name="login"),
    path("contact/", contact, name="contact")
]
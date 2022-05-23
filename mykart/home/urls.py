from django.contrib import admin
from django.urls import path
from home.views import home, about

urlpatterns = [
   path("", home, name="MyKart-home"),
   path("about", about, name="MyKart-about")
   
   ]
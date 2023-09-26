from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.logo,name='logo.html'),


]

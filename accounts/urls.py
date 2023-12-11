from django.urls import path,include
from . import views


urlpatterns=[
   
    path('registerUser/',views.registerUser,name="registerUser"),
    path('activate/<uidb64>/<token>/',views.activate,name='activate'),
    
]
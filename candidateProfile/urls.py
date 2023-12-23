from django.urls import path,include
from . import views

urlpatterns=[
   path('cprofile',views.registration_view,name='registration_view'),
   # path('cexpprofile',views.cexpprofile,name='cexpprofile'),
   
   
]  
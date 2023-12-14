from django.urls import path,include
from . import views

urlpatterns=[
   path('cprofile',views.registration_view,name='registration_view'),
#    path('cprofile',views.cprofile,name='cprofile'),
   # path('cexpprofile',views.cexpprofile,name='cexpprofile'),
   
   
]  
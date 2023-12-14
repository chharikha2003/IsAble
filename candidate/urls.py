from django.urls import path,include
from . import views

urlpatterns=[
   path('cprofilepage',views.cprofile,name='cprofilepage'),
   path('cprofile',views.cprofile,name='cprofile'),
   # path('cexpprofile',views.cexpprofile,name='cexpprofile'),
   
   
]  
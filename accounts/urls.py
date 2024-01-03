from django.urls import path,include
from . import views


urlpatterns=[
   
    path('registerUser/',views.registerUser,name="registerUser"),
    path('registerEmployer/',views.registerEmployer,name='registerEmployer'),
    path('candidateDashboard/',views.candidateDashboard,name='candidateDashboard'),
    path('employerDashboard/',views.employerDashboard,name='employerDashboard'),
    path('myAccount/',views.myAccount,name='myAccount'),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name='logout'),
    path('activate/<uidb64>/<token>/',views.activate,name='activate'),
    path('accounts/inactive/',views.account_inactive,name='account_inactive')
    
]
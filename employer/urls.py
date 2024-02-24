from django.urls import path,include
from . import views
from accounts import views as AccountViews
urlpatterns=[
   path('',AccountViews.employerDashboard,name='employer'),
   path('companyprofile',views.companyprofile_view,name='companyprofile_view'),
   
]  
from django.urls import path,include
from . import views

urlpatterns=[
   path('cprofile',views.main_registration_view,name='main_registration'),
   path('personal-details-ins',views.personal_details_ins,name='personal_details_ins'),
   path('education-details-ins',views.education_details_ins,name='education_details_ins'),
   path('experience-details-ins',views.experience_details_ins,name='experience_details_ins'),
   path('skills-details-ins',views.skills_details_ins,name='skills_details_ins'),
   path('certifications-details-ins',views.certifications_details_ins,name='certifications_details_ins'),
   path('projects-details-ins',views.projects_details_ins,name='projects_details_ins'),

   # path('cexpprofile',views.cexpprofile,name='cexpprofile'),
   
   
]  
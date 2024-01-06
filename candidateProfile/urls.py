from django.urls import path,include
from . import views


urlpatterns=[
   path('resume',views.resume,name='resume'),
   path('personal-details-ins',views.personal_details_ins,name='personal_details_ins'),
   path('education-details-ins',views.education_details_ins,name='education_details_ins'),
   path('experience-details-ins',views.experience_details_ins,name='experience_details_ins'),
   path('skills-details-ins',views.skills_details_ins,name='skills_details_ins'),
   path('keyAchievements-details-ins',views.keyAchievements_details_ins,name='keyAchievements_details_ins'),
   path('projects-details-ins',views.projects_details_ins,name='projects_details_ins'),
   path('languages-details-ins',views.languages_details_ins,name='languages_details_ins'),
   path('download_pdf/', views.download_pdf, name='download_pdf'),

   
   # path('cexpprofile',views.cexpprofile,name='cexpprofile'),
   
   
]  
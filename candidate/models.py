from django.db import models
from accounts.models import User, UserProfile
# Create your models here.
#this is for course and certificates
class Candidate(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    skills=models.CharField(max_length=400,default="skills")
    certificate_name=models.CharField(max_length=150)
    issued_by=models.CharField(max_length=100)

# class Experience(models.Model):
#     CURRENT=1
#     PREVIOUS=2
#     ROLE_CHOICE=(
#         (CURRENT,'Yes'),
#         (PREVIOUS,'No'),
#     )
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     Designation=models.CharField(max_length=100)
#     Organisation=models.CharField(max_length=100)
#     status=models.PositiveSmallIntegerField(choices=ROLE_CHOICE,blank=True,null=True)
#     descofjob=models.CharField(max_length=500)
#     worked_from = models.DateField()
#     worked_till = models.DateField()
    

   
    
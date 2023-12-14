from django.db import models

from accounts.models import User

# Create your models here.
class personal_details(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    profile_photo=models.ImageField(upload_to='candidate/profilephoto',default='default.jpg')
    phone_number=models.CharField(max_length=12,blank=True)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    country=models.CharField(max_length=20)


class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    highest_qualification=models.CharField(max_length=20)
    specialization=models.CharField(max_length=20)
    institute=models.CharField(max_length=20)
    start_year=models.DateField();
    end_year=models.DateField();

class Experience(models.Model):
    
    ROLE_CHOICE=(
        (1,'Yes'),
        (2,'No'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Designation=models.CharField(max_length=100)
    Organisation=models.CharField(max_length=100)
    status=models.PositiveSmallIntegerField(choices=ROLE_CHOICE,blank=True,null=True)
    descofjob=models.CharField(max_length=500)
    worked_from = models.DateField()
    worked_till = models.DateField()

class Skills(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    skill=models.CharField(max_length=100)


class Certifications(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    certificate=models.CharField(max_length=100)
    issued_by=models.CharField(max_length=100)
    date_issued=models.DateField()


class Projects(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title=models.CharField(max_length=100)
    link=models.CharField(max_length=100)
    desc=models.CharField(max_length=500)

# class Languages(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     title=models.CharField(max_length=100)
#     link=models.CharField(max_length=100)
#     desc=models.CharField(max_length=500)

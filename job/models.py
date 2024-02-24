from django.db import models
from django.utils import timezone

from employer.models import Employer
# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Job(models.Model):
    CATEGORY_CHOICE=(
        ("Internship",'Internship'),
        ("Full Time",'FULL TIME'),
        ("Hybrid",'HYBRID'),
        ("Remote",'REMOTE')
    )
    EXPERIENCE_CHOICES = [
        ('Entry Level', 'Entry Level'),
        ('1 Year', '1 Year'),
        ('2 Years', '2 Years'),
        ('3 Years', '3 Years'),
        ('4 Years', '4 Years'),
        ('5+ Years', '5+ Years'),
    ]
    MINIMUM_QUALIFICATION_CHOICES = [
        ('10th Pass', '10th Pass'),
        ('12th Pass', '12th Pass'),
        ('Bachelor\'s Degree', 'Bachelor\'s Degree'),
        ('Master\'s Degree', 'Master\'s Degree'),
        ('Ph.D.', 'Ph.D.'),
    ]
    CITY_CHOICES = [
        ('All','All'),
        ('Mumbai', 'Mumbai'),
        ('Bangalore', 'Bangalore'),
        ('Delhi','Delhi'),
        ('Hyderabad','Hyderabad'),
        ('Chennai','Chennai'),
        ('Lucknow','Lucknow')
    ]
    title =models.CharField(max_length=255)
    city=models.CharField(max_length=100,choices=CITY_CHOICES, blank=True, null=True,default="Choose City")
    category=models.CharField(max_length=100,choices=CATEGORY_CHOICE,blank=True,null=True,default="Choose Category")
    description = models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    company=models.ForeignKey(Employer,on_delete=models.CASCADE)
    disability_type = models.CharField(max_length=100, choices=[
        ('All','All'),
        ('Blindness', 'Blindness'),
        ('Cerebral Palsy', 'Cerebral Palsy'),
        ('Hearing impairment','Hearing impairment'),
        ('Locomotor disability','Locomotor disability'),
        ('Mental illness','Mental illness'),
        ('Haemophilia','Haemophilia')
    ], blank=True, null=True)

    salary=models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    experience = models.CharField(max_length=50,choices=EXPERIENCE_CHOICES)
    vacancy=models.IntegerField(blank=True, null=True)
    min_qualification=models.CharField(max_length=50, choices=MINIMUM_QUALIFICATION_CHOICES, blank=True, null=True)
    application_lastdate=models.DateTimeField(default=timezone.now)
    application_link=models.URLField(blank=True)



    def __str__(self):
        return self.title
    
   
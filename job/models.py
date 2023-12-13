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
    title =models.CharField(max_length=255)
    
    city=models.CharField(max_length=100)
    category=models.CharField(max_length=100,choices=CATEGORY_CHOICE,blank=True,null=True,default="Choose Category")
    description = models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    company=models.ForeignKey(Employer,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
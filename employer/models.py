from django.db import models
from accounts.utils import send_notification
from datetime import time,date,datetime
from accounts.models import User, UserProfile


# Create your models here.
class Employer(models.Model):

    INDUSTRY_CHOICE=(
        ('All','All'),
        ('Agriculture','Agriculture'),
        ('Automotive','Automotive'),
        ('Banking and Finance','Banking and Finance'),
        ('Biotechnology','Biotechnology'),
        ('Construction','Construction'),
        ('Education','Education'),
        ('Energy','Energy'),
        ('Entertainment','Entertainment'),
        ('Healthcare','Healthcare'),
        ('Hospitality','Hospitality'),
        ('Information Technology (IT)','Information Technology (IT)'),
        ('Manufacturing','Manufacturing'),
        ('Marketing and Advertising','Marketing and Advertising'),
        ('Media','Media'),
        ('Non-Profit','Non-Profit'),
        ('Retail','Retail'),
        ('Telecommunications','Telecommunications'),
        ('Transportation','Transportation'),
        ('Travel and Tourism','Travel and Tourism')
    )

    SECTOR_CHOICE=(
        ('All','All'),
        ('Private','Private'),
        ('Public','Public')
    )
    user=models.OneToOneField(User,related_name='user',on_delete=models.CASCADE)
    user_profile=models.OneToOneField(UserProfile,related_name='userprofile',on_delete=models.CASCADE)
    company_name=models.CharField(max_length=50)
    company_license=models.ImageField(upload_to='company/license')
    company_logo=models.ImageField(upload_to='company/logo')
    company_desc=models.CharField(max_length=500)
    company_address=models.CharField(max_length=100)
    company_phone=models.IntegerField()
    company_email=models.EmailField(max_length=50,unique=True)
    company_website=models.URLField()
    twitter = models.URLField()
    linkedin = models.URLField()
    accessibility_features=models.CharField(max_length=500,default='')
    support_services=models.CharField(max_length=500)
    inclusive_hiring_practices=models.CharField(max_length=500)
    is_approved=models.BooleanField(default=False)
    sector=models.CharField(max_length=50,choices=SECTOR_CHOICE)
    industry_type=models.CharField(max_length=50,choices=INDUSTRY_CHOICE)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name
    
    def save(self,*args,**kwargs):
        if self.pk is not None:
            #Update
            orig=Employer.objects.get(pk=self.pk)
            if orig.is_approved!=self.is_approved:
                mail_template="accounts/emails/admin_approval_email.html"
                context={
                    'user':self.user,
                    'is_approved':self.is_approved,
                }
                if self.is_approved==True:
                    #send notifictaion email
                    mail_subject="Congratulations! Your Company has been approved."
                   
                    send_notification(mail_subject,mail_template,context)
                else:
                    #Send notification email
                    mail_subject=""
                    send_notification(mail_subject,mail_template,context)
        return super(Employer,self).save(*args,**kwargs)
    
class Employer_Detailed(models.Model):
    user=models.OneToOneField(User,related_name='user_emp',on_delete=models.CASCADE)
    description = models.TextField()
    industry = models.CharField(max_length=100)
    founded_year = models.PositiveIntegerField()
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='company_logos/', null=True, blank=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
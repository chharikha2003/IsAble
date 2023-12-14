from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages,auth
from accounts.forms import UserForm
from accounts.models import User, UserProfile
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from accounts.utils import detectUser, send_verification_email
from employer.forms import Employerform
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required,user_passes_test
from candidateProfile.models import *
from employer.models import Employer


#Restrict the customer from accessing the vendor page

@login_required(login_url='login')
def myAccount(request):
    user=request.user
    redirectUrl=detectUser(user)
    return redirect(redirectUrl)


def check_role_candidate(user):
    if user.role==1:
        return True
    else:
        raise PermissionDenied
    
def check_role_employer(user):
    if user.role==2:
        return True
    else:
        raise PermissionDenied
    
def registerUser(request):
    
    if request.method=='POST':
        form=UserForm(request.POST)
        
        if form.is_valid():
            
            
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.CANDIDATE
            user.save()
            email_subject='Please activate your account'
            email_template='accounts/emails/account_verification_email.html'
            send_verification_email(request,user,email_subject,email_template)
            messages.success(request,"your account has been successfully registered")
            


            return redirect('login')
        else:
            print(form.errors)
    else:
        form=UserForm()
    context={
        'form':form
    }
    return render(request,'accounts/registerUser.html',context)


def registerEmployer(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are already logged in!')
        return redirect('myAccount')
    elif request.method=='POST':
        #store the data and create the user
        form=UserForm(request.POST)
        e_form=Employerform(request.POST,request.FILES)
        if form.is_valid() and e_form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            username=form.cleaned_data['first_name']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            user.role=User.EMPLOYER
            user.save()
            employer=e_form.save(commit=False)
            employer.user=user 
            company_name=e_form.cleaned_data['company_name']
            user_profile=UserProfile.objects.get(user=user)
            employer.user_profile=user_profile
            employer.save()

            #Send verification email
            mail_subject='Please activate your account'
            email_template='accounts/emails/account_verification_email.html'
            send_verification_email(request,user,mail_subject,email_template)
            
            messages.success(request, 'Your account has been registered successfully! Please wait for the approval')
            return redirect('login')
        else:

            print('invalid form')
            print(form.errors)

    else:
        form=UserForm()
        e_form=Employerform()

    context={
        'form':form,
        'e_form':e_form,
    }
    return render(request,'accounts/registerEmployer.html',context)
def activate(request,uidb64,token):
    try:
        uid=urlsafe_base64_decode(uidb64).decode()
        user=User._default_manager.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        user=None
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active=True
        user.save()
        messages.success(request,"congratulations your account is activated")
        return redirect('registerUser')
    else:
        messages.error(request,'Invalid link')
        return redirect('registerUser')    
    
def login(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are already logged in!')
        return redirect('myAccount')
    elif request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']

        user=auth.authenticate(email=email,password=password)

        if user is not None:
            print("yayy")
            auth.login(request,user)
            messages.success(request,'You are now logged in.')
            return redirect('registration_view')
        else:
            print('errorshai')
            messages.error(request,'Invalid login credentials')
            return redirect('login')
    return render(request,'accounts/login.html')

def logout(request):
    auth.logout(request)
    messages.info(request,"You logged out")
    return redirect("login")



login_required(login_url='login')
@user_passes_test(check_role_candidate)
def candidateDashboard(request):
    personal_details_data = personal_details.objects.filter(user=request.user)
    Education_data = Education.objects.filter(user=request.user)
    Experience_data = Experience.objects.filter(user=request.user)
    Skills_data = Skills.objects.filter(user=request.user)
    Certifications_data = Certifications.objects.filter(user=request.user)
    Projects_data = Projects.objects.filter(user=request.user)

    context={
        'personal_details_data' : personal_details_data,
        'Education_data' : Education_data,
        'Experience_data' : Experience_data,
        'Skills_data' : Skills_data,
        'Certifications_data' : Certifications_data,
        'Projects_data' : Projects_data
        
    }

    return render(request,'accounts/candidateDashboard.html',context)

@login_required(login_url='login')
@user_passes_test(check_role_employer)
def employerDashboard(request):
    emp=Employer.objects.filter(user=request.user)
    employer_details_data = personal_details.objects.filter(user=request.user)  
    return render(request,'accounts/employerDashboard.html',{'employer_details_data':employer_details_data})
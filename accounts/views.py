from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages,auth
from accounts.forms import UserForm
from accounts.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from accounts.utils import send_verification_email
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
            user.role = User.CUSTOMER
            user.save()
            email_subject='Please activate your account'
            email_template='accounts/emails/account_verification_email.html'
            send_verification_email(request,user,email_subject,email_template)
            messages.success(request,"your account has been successfully registered")
            


            return redirect('registerUser')
        else:
            print(form.errors)
    else:
        form=UserForm()
    context={
        'form':form
    }
    return render(request,'accounts/registerUser.html',context)
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
        messages.warning(request,"you are already logged in")
        return redirect('login')
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=auth.authenticate(email=email,password=password)
        
        if user!=None:
            auth.login(request,user)
            print("login")
            messages.success(request,'You are now loggedIn')
            return redirect('home')
        else:
            print("ddd")
            messages.error(request,'Invalid Credentials')
            return redirect('home')

    return render(request,'accounts/login.html')

def logout(request):
    auth.logout(request)
    messages.info(request,"You logged out")
    return redirect("login")
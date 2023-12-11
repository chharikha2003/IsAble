from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages,auth
from accounts.forms import UserForm
from accounts.models import User
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
            


            return redirect('registerUser')
        else:
            print(form.errors)
    else:
        form=UserForm()
    context={
        'form':form
    }
    return render(request,'accounts/registerUser.html',context)

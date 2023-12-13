from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required,user_passes_test
from django.shortcuts import get_object_or_404

from accounts.models import User
import candidate
from candidate.forms import CandidateForm, ExperienceForm
from candidate.models import Candidate, Experience
def check_role_candidate(user):
    if user.role==1:
        return True
    else:
        raise PermissionDenied
def cprofilepage(request,render):
    return render(request,'candidate/cprofile.html')

login_required(login_url='login')
@user_passes_test(check_role_candidate)

def cprofile(request):
    
    if request.method=='POST':
        form=CandidateForm(request.POST)
        
        if form.is_valid():
            cand=Candidate()
            cand.user=request.user
            cand.skills=form.cleaned_data['skills']
            cand.certificate_name = form.cleaned_data['certificate_name']
            cand.issued_by = form.cleaned_data['issued_by']
           
            cand.save()
            return redirect('cprofile')
        else:
            print(form.errors)
    else:
        form=CandidateForm()
    context={
        'form':form
    }
    return render(request,'candidate/cprofile.html',context)






login_required(login_url='login')
@user_passes_test(check_role_candidate)

def cexpprofile(request):
    
    if request.method=='POST':
        expform=ExperienceForm(request.POST)
        
        if expform.is_valid():
            expform_save =expform.save(commit=False)
            expform_save.user=request.user
            
            expform.save()
            return redirect('cprofile')
        else:
            print(expform.errors)
    else:
        expform=ExperienceForm()
    context={
        'expform':expform
    }
    return render(request,'candidate/cprofile.html',context)




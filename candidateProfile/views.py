from django.shortcuts import redirect, render
from .models import personal_details
from .forms import *
# Create your views here.
def personal_details_ins(request):
    if request.method=='POST':
        personal_details_form=PersonalDetailsForm(request.POST)
        
        if personal_details_form.is_valid():
            personal_details_form_save =personal_details_form.save(commit=False)
            personal_details_form_save.user=request.user
            personal_details_form.save()
            return redirect('personal_details_form')
        else:
            print(personal_details_form.errors)
    else:
        personal_details_form=PersonalDetailsForm()
    context={

        'personal_details_form':personal_details_form
    }
    return render(request,'candidate/cprofile.html',context)


def registration_view(request):

    if request.method == 'POST':
        personal_details_form = PersonalDetailsForm(request.POST,request.FILES)
        education_form = EducationForm(request.POST)
        experience_form = ExperienceForm(request.POST)
        skills_form=SkillsForm(request.POST)
        certifications_form=CertificationsForm(request.POST)
        projects_form=ProjectsForm(request.POST)

        if personal_details_form.is_valid() and education_form.is_valid() and experience_form.is_valid() and skills_form.is_valid() and certifications_form.is_valid() and projects_form.is_valid() :
            # Save each form individually to the respective models
            print('valid')
            personal_details = personal_details_form.save(commit=False)
            personal_details.user = request.user
            personal_details.save()

            education = education_form.save(commit=False)
            education.user = request.user
            education.save()

            experience = experience_form.save(commit=False)
            experience.user = request.user
            experience.save()

            skills= skills_form.save(commit=False)
            skills.user = request.user
            skills.save()

            certifications = certifications_form.save(commit=False)
            certifications.user = request.user
            certifications.save()

            projects = projects_form.save(commit=False)
            projects.user = request.user
            projects.save()

            print('savedd')
            # Redirect or do something else
            return redirect('candidateDashboard')
        else:
            print('error')
            print(personal_details_form.errors)
            print(education_form.errors)
            print(experience_form.errors)
            print(skills_form.errors)
            print(certifications_form.errors)
            print(projects_form.errors)

    else:
        
        personal_details_form = PersonalDetailsForm()
        education_form = EducationForm()
        experience_form = ExperienceForm()
        skills_form=SkillsForm()
        certifications_form=CertificationsForm()
        projects_form=ProjectsForm()

        

    return render(request, 'candidate/cprofile.html', {
        'personal_details_form': personal_details_form,
        'education_form': education_form,
        'experience_form': experience_form,
        'skills_form': skills_form,
        'certifications_form': certifications_form,
        'projects_form': projects_form
        
    })
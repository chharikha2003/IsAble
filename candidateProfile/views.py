from django.forms import formset_factory
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib import messages
# Create your views here.


def personal_details_ins(request):
    if request.method=='POST':
        personal_details_form = PersonalDetailsForm(request.POST,request.FILES)
        if personal_details_form.is_valid():
            print("Valid")
            personal_details_form_save = personal_details_form.save(commit=False)
            personal_details_form_save.created_by = request.user
            personal_details_form_save.updated_by = request.user
            personal_details_form_save.user = request.user
            personal_details_form_save.save()
            print("saveddd")
            return redirect("main_registration")
        else:
            print("errors", personal_details_form.errors)
            for error_messages in personal_details_form.errors.values():
                for error_message in error_messages:
                    messages.error(request, error_message)
            return redirect("main_registration")
    personal_details_form = PersonalDetailsForm()
    
    personal_details_table_data = personal_details.objects.filter(  
        Q(created_by=1) | Q(created_by=request.user))

    print(personal_details_table_data)

    data = {
        "personal_details_form": personal_details_form,
        "personal_details_table_data": personal_details_table_data,
    }
    return render(request, "candidate/cprofile.html", data)


def education_details_ins(request):
    if request.method=='POST':
        education_details_form = EducationForm(request.POST)
        if education_details_form.is_valid():
            print("Valid")
            education_details_form_save = education_details_form.save(commit=False)
            education_details_form_save.created_by = request.user
            education_details_form_save.updated_by = request.user
            education_details_form_save.user = request.user
            education_details_form_save.save()
            print("saveddd")
            return redirect("main_registration")
        else:
            print("errors", education_details_form.errors)
            for error_messages in education_details_form.errors.values():
                for error_message in error_messages:
                    messages.error(request, error_message)
            return redirect("main_registration")
    education_details_form = EducationForm()
    
    education_detail_table_data = Education.objects.filter(  
        Q(created_by=1) | Q(created_by=request.user))

    print(education_detail_table_data)

    data = {
        "education_details_form": education_details_form,
        "education_detail_table_data": education_detail_table_data,
    }
    return render(request, "candidate/cprofile.html", data)


def experience_details_ins(request):
    if request.method=='POST':
        experience_details_form = ExperienceForm(request.POST,request.FILES)
        if experience_details_form.is_valid():
            print("Valid")
            experience_details_form_save = experience_details_form.save(commit=False)
            experience_details_form_save.created_by = request.user
            experience_details_form_save.updated_by = request.user
            experience_details_form_save.user = request.user
            experience_details_form_save.save()
            print("saveddd")
            return redirect("main_registration")
        else:
            print("errors", experience_details_form.errors)
            for error_messages in experience_details_form.errors.values():
                for error_message in error_messages:
                    messages.error(request, error_message)
            return redirect("main_registration")
    experience_details_form = ExperienceForm()
    
    experience_details_table_data = Experience.objects.filter(  
        Q(created_by=1) | Q(created_by=request.user))

    print(experience_details_table_data)

    data = {
        "experience_details_form": experience_details_form,
        "experience_details_table_data": experience_details_table_data,
    }
    return render(request, "candidate/cprofile.html", data)


def skills_details_ins(request):
    if request.method=='POST':
        skills_details_form = SkillsForm(request.POST,request.FILES)
        if skills_details_form.is_valid():
            print("Valid")
            skills_details_form_save = skills_details_form.save(commit=False)
            skills_details_form_save.created_by = request.user
            skills_details_form_save.updated_by = request.user
            skills_details_form_save.user = request.user
            skills_details_form_save.save()
            print("saveddd")
            return redirect("main_registration")
        else:
            print("errors", skills_details_form.errors)
            for error_messages in skills_details_form.errors.values():
                for error_message in error_messages:
                    messages.error(request, error_message)
            return redirect("main_registration")
    skills_details_form = SkillsForm()
    
    skills_details_table_data = Skills.objects.filter(  
        Q(created_by=1) | Q(created_by=request.user))

    print(skills_details_table_data)

    data = {
        "skills_details_form": skills_details_form,
        "skills_details_table_data": skills_details_table_data,
    }
    return render(request, "candidate/cprofile.html", data)

def certifications_details_ins(request):
    if request.method=='POST':
        certifications_details_form = CertificationsForm(request.POST,request.FILES)
        if certifications_details_form.is_valid():
            print("Valid")
            certifications_details_form_save = certifications_details_form.save(commit=False)
            certifications_details_form_save.created_by = request.user
            certifications_details_form_save.updated_by = request.user
            certifications_details_form_save.user = request.user
            certifications_details_form_save.save()
            print("saveddd")
            return redirect("main_registration")
        else:
            print("errors", certifications_details_form.errors)
            for error_messages in certifications_details_form.errors.values():
                for error_message in error_messages:
                    messages.error(request, error_message)
            return redirect("main_registration")
    certifications_details_form = CertificationsForm()
    
    certifications_details_table_data = Certifications.objects.filter(  
        Q(created_by=1) | Q(created_by=request.user))

    print(certifications_details_table_data)

    data = {
        "certifications_details_form": certifications_details_form,
        "certifications_details_table_data": certifications_details_table_data,
    }
    return render(request, "candidate/cprofile.html", data)

def projects_details_ins(request):
    if request.method=='POST':
        projects_details_form = ProjectsForm(request.POST,request.FILES)
        if projects_details_form.is_valid():
            print("Valid")
            projects_details_form_save = projects_details_form.save(commit=False)
            projects_details_form_save.created_by = request.user
            projects_details_form_save.updated_by = request.user
            projects_details_form_save.user = request.user
            projects_details_form_save.save()
            print("saveddd")
            return redirect("main_registration")
        else:
            print("errors", projects_details_form.errors)
            for error_messages in projects_details_form.errors.values():
                for error_message in error_messages:
                    messages.error(request, error_message)
            return redirect("main_registration")
    projects_details_form = ProjectsForm()
    
    projects_details_table_data = Projects.objects.filter(  
        Q(created_by=1) | Q(created_by=request.user))

    print(projects_details_table_data)

    data = {
        "projects_details_form": projects_details_form,
        "projects_details_table_data": projects_details_table_data,
    }
    return render(request, "candidate/cprofile.html", data)


def main_registration_view(request):
    personal_details_form = PersonalDetailsForm()
    education_form = EducationForm()
    experience_form = ExperienceForm()
    projects_form = ProjectsForm()
    skills_form = SkillsForm()
    certifications_form = CertificationsForm()

    return render(request, 'candidate/cprofile.html', {
        'personal_details_form': personal_details_form,
        'education_form': education_form,
        'experience_form': experience_form,
        'projects_form': projects_form,
        'skills_form':skills_form,
        'certifications_form':certifications_form
    })

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
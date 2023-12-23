from django.forms import formset_factory
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *
# Create your views here.


def registration_view(request):
    personal_details_inst=get_object_or_404(personal_details,user=request.user)
    education_inst=get_object_or_404(Education,user=request.user)
    experience_inst=get_object_or_404(Experience,user=request.user)
    skills_inst=get_object_or_404(Skills,user=request.user)
    certifications_inst=get_object_or_404(Certifications,user=request.user)
    projects_inst=get_object_or_404(Projects,user=request.user)
    EducationFormSet=formset_factory(EducationForm, extra=1)

    if request.method == 'POST':
        personal_details_form = PersonalDetailsForm(request.POST,request.FILES,instance=personal_details_inst)
        education_formset = EducationFormSet(request.POST,prefix='edu',instance=education_inst)
        experience_form = ExperienceForm(request.POST,instance=experience_inst)
        skills_form=SkillsForm(request.POST,instance=skills_inst)
        certifications_form=CertificationsForm(request.POST,instance=certifications_inst)
        projects_form=ProjectsForm(request.POST,instance=projects_inst)

        if personal_details_form.is_valid() and education_formset.is_valid() and experience_form.is_valid() and skills_form.is_valid() and certifications_form.is_valid() and projects_form.is_valid() :
            # Save each form individually to the respective models
            print('valid')
            personal_detail = personal_details_form.save(commit=False)
            personal_detail.user = request.user
            personal_detail.save()

            education = education_formset.save(commit=False)
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
            print(education_formset.errors)
            print(experience_form.errors)
            print(skills_form.errors)
            print(certifications_form.errors)
            print(projects_form.errors)

    else:
        
        personal_details_form = PersonalDetailsForm(instance=personal_details_inst)
        education_formset = EducationFormSet(prefix='edu',instance=education_inst)
        experience_form = ExperienceForm(instance=experience_inst)
        skills_form=SkillsForm(instance=skills_inst)
        certifications_form=CertificationsForm(instance=certifications_inst)
        projects_form=ProjectsForm(instance=projects_inst)

        

    return render(request, 'candidate/cprofile.html', {
        'personal_details_form': personal_details_form,
        'education_formset': education_formset,
        'experience_form': experience_form,
        'skills_form': skills_form,
        'certifications_form': certifications_form,
        'projects_form': projects_form
        
    })



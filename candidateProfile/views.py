from django.forms import formset_factory
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import get_template
import weasyprint
import os
os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\bin")
from weasyprint import HTML
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
            return redirect("education_details_ins")
        else:
            print("errors", personal_details_form.errors)
            for error_messages in personal_details_form.errors.values():
                for error_message in error_messages:
                    messages.error(request, error_message)
            return redirect("personal_details_ins")
    personal_details_form = PersonalDetailsForm()
    
    # personal_details_table_data = personal_details.objects.filter(  
    #     Q(created_by=1) | Q(created_by=request.user))

    # print(personal_details_table_data)

    data = {
        "personal_details_form": personal_details_form,
        
    }
    return render(request, "candidate/personal_details.html", data)


# def education_details_ins(request):
#     EducationFormSet=formset_factory(EducationForm,extra=1)
#     if request.method=='POST':
#         education_details_formset = EducationFormSet(request.POST,prefix='education')
#         if education_details_formset.is_valid():
#             for education_details_form in education_details_formset:
#                 print("Valid")
#                 education_details_form_save = education_details_form.save(commit=False)
#                 education_details_form_save.created_by = request.user
#                 education_details_form_save.updated_by = request.user
#                 education_details_form_save.user = request.user
#                 education_details_form_save.save()
#             print("saveddd")
#             return redirect("main_registration")
#     else:
#         education_details_formset=EducationFormSet(prefix='education')
        

#     data = {
#         "education_details_formset": education_details_formset,
        
#     }
#     return render(request, "candidate/cprofile.html", data)

def education_details_ins(request):
    EducationFormSet = formset_factory(EducationForm, extra=1, can_delete=True)

    if request.method == 'POST':
        education_details_formset = EducationFormSet(request.POST, prefix='education')
        if education_details_formset.is_valid():
            for form in education_details_formset:
                if form.cleaned_data.get('DELETE'):
                    # If form marked for deletion, skip saving
                    continue
                education_details_form_save = form.save(commit=False)
                education_details_form_save.created_by = request.user
                education_details_form_save.updated_by = request.user
                education_details_form_save.user = request.user
                education_details_form_save.save()
            messages.success(request, 'Education details saved successfully.')
            return redirect("experience_details_ins")
        else:
            print("error")
            messages.error(request, 'Education formset is invalid. Please correct the errors.')
    else:
        education_details_formset = EducationFormSet(prefix='education')

    data = {
        "education_details_formset": education_details_formset,
    }
    return render(request, "candidate/education_details.html", data)


def experience_details_ins(request):
    ExperienceFormSet = formset_factory(ExperienceForm, extra=1, can_delete=True)

    if request.method=='POST':
        experience_details_formset = ExperienceFormSet(request.POST,prefix='experience')
        if experience_details_formset.is_valid():
            for form in experience_details_formset:
                if form.cleaned_data.get('DELETE'):
                    # If form marked for deletion, skip saving
                    continue
                experience_details_form_save = form.save(commit=False)
                experience_details_form_save.created_by = request.user
                experience_details_form_save.updated_by = request.user
                experience_details_form_save.user = request.user
                experience_details_form_save.save()
            messages.success(request, 'Experience details saved successfully.')
            return redirect("skills_details_ins")
        else:
            messages.error(request, 'Experience formset is invalid. Please correct the errors.')
    else:
        experience_details_formset = ExperienceFormSet(prefix='experience')

    data = {
        "experience_details_formset": experience_details_formset,
    }
    return render(request, "candidate/experience_details.html", data)


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
            return redirect("projects_details_ins")
        else:
            print("errors", skills_details_form.errors)
            for error_messages in skills_details_form.errors.values():
                for error_message in error_messages:
                    messages.error(request, error_message)
            return redirect("skills_details_ins")
    skills_details_form = SkillsForm()
    
    # skills_details_table_data = Skills.objects.filter(  
    #     Q(created_by=1) | Q(created_by=request.user))

    # print(skills_details_table_data)

    data = {
        "skills_details_form": skills_details_form,
    }
    return render(request, "candidate/skills_details.html", data)

def projects_details_ins(request):
    ProjectsFormSet = formset_factory(ProjectsForm, extra=1, can_delete=True)

    if request.method=='POST':
        projects_details_formset = ProjectsFormSet(request.POST,prefix='projects')
        if projects_details_formset.is_valid():
            for form in projects_details_formset:
                if form.cleaned_data.get('DELETE'):
                    # If form marked for deletion, skip saving
                    continue
                projects_details_form_save = form.save(commit=False)
                projects_details_form_save.created_by = request.user
                projects_details_form_save.updated_by = request.user
                projects_details_form_save.user = request.user
                projects_details_form_save.save()
            messages.success(request, 'Projects details saved successfully.')
            return redirect("keyAchievements_details_ins")
        else:
            messages.error(request, 'Projects formset is invalid. Please correct the errors.')
    else:
        projects_details_formset = ProjectsFormSet(prefix='projects')

    data = {
        "projects_details_formset": projects_details_formset,
    }
    return render(request, "candidate/projects_details.html", data)

def keyAchievements_details_ins(request):
    keyAchievementsFormSet = formset_factory(keyAchievementsForm, extra=1, can_delete=True)

    if request.method=='POST':
        keyAchievements_details_formset = keyAchievementsFormSet(request.POST,prefix='keyAchievements')
        if keyAchievements_details_formset.is_valid():
            for form in keyAchievements_details_formset:
                if form.cleaned_data.get('DELETE'):
                    # If form marked for deletion, skip saving
                    continue
                keyAchievements_details_form_save = form.save(commit=False)
                keyAchievements_details_form_save.created_by = request.user
                keyAchievements_details_form_save.updated_by = request.user
                keyAchievements_details_form_save.user = request.user
                keyAchievements_details_form_save.save()
            messages.success(request, 'Key Achievements details saved successfully.')
            return redirect("languages_details_ins")
        else:
            messages.error(request, 'Key Achievements formset is invalid. Please correct the errors.')
    else:
        keyAchievements_details_formset = keyAchievementsFormSet(prefix='keyAchievements')

    data = {
        "keyAchievements_details_formset": keyAchievements_details_formset,
    }
    return render(request, "candidate/keyAchievements_details.html", data)
    
def languages_details_ins(request):
    LanguagesFormSet = formset_factory(LanguagesForm, extra=1, can_delete=True)

    if request.method=='POST':
        languages_details_formset = LanguagesFormSet(request.POST,prefix='languages')
        if languages_details_formset.is_valid():
            for form in languages_details_formset:
                if form.cleaned_data.get('DELETE'):
                    # If form marked for deletion, skip saving
                    continue
                languages_details_form_save = form.save(commit=False)
                languages_details_form_save.created_by = request.user
                languages_details_form_save.updated_by = request.user
                languages_details_form_save.user = request.user
                languages_details_form_save.save()
            messages.success(request, 'Languages details saved successfully.')
            return redirect("candidateDashboard")
        else:
            messages.error(request, 'Languages formset is invalid. Please correct the errors.')
    else:
        languages_details_formset = LanguagesFormSet(prefix='languages')

    data = {
        "languages_details_formset": languages_details_formset,
    }
    return render(request, "candidate/languages_details.html", data)


def resume(request):
    personal_details_data = personal_details.objects.filter(user=request.user)
    Education_data = Education.objects.filter(user=request.user)
    Experience_data = Experience.objects.filter(user=request.user)
    Skills_data = Skills.objects.filter(user=request.user)
    keyAchievements_data = keyAchievements.objects.filter(user=request.user)
    languages_data = Languages.objects.filter(user=request.user)

    Projects_data = Projects.objects.filter(user=request.user)
    profile_photo_url = request.build_absolute_uri(personal_details_data[0].profile_photo.url) if personal_details_data else ''

    print(len(Education_data))

    context={
        'personal_details_data' : personal_details_data,
        'Education_data' : Education_data,
        'Experience_data' : Experience_data,
        'Skills_data' : Skills_data,
        'keyAchievements_data' : keyAchievements_data,
        'Projects_data' : Projects_data,
        'profile_photo_url': profile_photo_url,
        'languages_data':languages_data
    }

    return render(request,"candidate/resume.html",context)

def download_pdf(request):
    # Get the HTML template

    template = get_template('candidate/resume.html')

    personal_details_data = personal_details.objects.filter(user=request.user)
    Education_data = Education.objects.filter(user=request.user)
    Experience_data = Experience.objects.filter(user=request.user)
    Skills_data = Skills.objects.filter(user=request.user)
    keyAchievements_data = keyAchievements.objects.filter(user=request.user)
    languages_data = Languages.objects.filter(user=request.user)
    Projects_data = Projects.objects.filter(user=request.user)
    profile_photo_url = request.build_absolute_uri(personal_details_data[0].profile_photo.url) if personal_details_data else ''
    print(personal_details_data[0].profile_photo.url)
    print(len(Education_data))

    context={
        'personal_details_data' : personal_details_data,
        'Education_data' : Education_data,
        'Experience_data' : Experience_data,
        'Skills_data' : Skills_data,
        'keyAchievements_data' : keyAchievements_data,
        'Projects_data' : Projects_data,
        'profile_photo_url': profile_photo_url,
        'languages_data':languages_data
        
    }
    html = template.render(context)

    # Generate PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Resume.pdf"'
    weasyprint.HTML(string=html).write_pdf(response)

    return response
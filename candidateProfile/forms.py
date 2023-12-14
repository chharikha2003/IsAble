from django import forms
from .models import *
from accounts.validators import allow_only_images_validator

class PersonalDetailsForm(forms.ModelForm):
    profile_photo=forms.FileField(widget=forms.FileInput(attrs={'class':'btn btn-info'}),validators=[allow_only_images_validator])
    class Meta:
        model = personal_details
        fields = ['phone_number','city','state','country','profile_photo']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['highest_qualification','specialization','institute','start_year','end_year']

class ExperienceForm(forms.ModelForm):
     class Meta:
        model = Experience
        fields = ['Designation','Organisation','status','descofjob','worked_from','worked_till']

        status_choices = (
            ("", "None"),
            ("1", "Yes"),
            ("2", "No"),
           
        )

        widgets = {
            "Designation": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Designation",
                }
            ),
            "Organisation": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Organisation",
                }
            ),
            "status": forms.Select(
                choices=status_choices,
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Are you a current employee of the organisation",
                }
            ),
            "descofjob": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Job Description",
                }
            ),

            "worked_from": forms.DateInput(
               
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Worked From",
                }
            ),

            "worked_till": forms.DateInput(
                

                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Worked Till",
                }
            ),
            
        }

class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ['skill']

class CertificationsForm(forms.ModelForm):
    class Meta:
        model = Certifications
        fields = ['certificate','issued_by','date_issued']

class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['title','link','desc']


        

        
# class ExperienceForm(forms.ModelForm):

#     class Meta:
#         model = Experience
#         fields = ['Designation','Organisation','status','descofjob','worked_from','worked_till']
#         widgets = {
#             'worked_from': DateInput(),
#         }
#         labels = {
#             "Designation": "Designation",
#             "Organisation": "Organisation",
#             "Are You Currently Employeed": "status",
#             "Job Description": "descofjob",
#             "Worked from": "worked_from",
#             "Worked Till": "worked_till",
            
#         }
        
        
#         status_choices = (
#             ("", "None"),
#             ("1", "Yes"),
#             ("2", "No"),
           
#         )
        

#         widgets = {
#             "Designation": forms.TextInput(
#                 attrs={
#                     "class": "form-control",
#                     "style": "width: 100%; margin-bottom: 20px;",
#                     "placeholder": "Designation",
#                 }
#             ),
#             "Organisation": forms.TextInput(
#                 attrs={
#                     "class": "form-control",
#                     "style": "width: 100%; margin-bottom: 20px;",
#                     "placeholder": "Organisation",
#                 }
#             ),
#             "status": forms.Select(
#                 choices=status_choices,
#                 attrs={
#                     "class": "form-control",
#                     "style": "width: 100%; margin-bottom: 20px;",
#                     "placeholder": "Are you a current employee of the organisation",
#                 }
#             ),
#             "descofjob": forms.TextInput(
#                 attrs={
#                     "class": "form-control",
#                     "style": "width: 100%; margin-bottom: 20px;",
#                     "placeholder": "Job Description",
#                 }
#             ),

#             "worked_from": forms.DateInput(
               
#                 attrs={
#                     "class": "form-control",
#                     "style": "width: 100%; margin-bottom: 20px;",
#                     "placeholder": "Worked From",
#                 }
#             ),

#             "worked_till": forms.DateInput(
                

#                 attrs={
#                     "class": "form-control",
#                     "style": "width: 100%; margin-bottom: 20px;",
#                     "placeholder": "Worked Till",
#                 }
#             ),
            
#         }
        

    
   
from django import forms
from .models import *
from accounts.validators import allow_only_images_validator

class PersonalDetailsForm(forms.ModelForm):
    profile_photo=forms.FileField(widget=forms.FileInput(attrs={'class':'btn btn-info'}),validators=[allow_only_images_validator])
    class Meta:
        model = personal_details
        fields = ['phone_number','city','state','country','profile_photo','bio']

        widgets = {
            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Phone number",
                }
            ),
            "city": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "City",
                }
            ),
            "state": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "State",
                }
            ),
            "country": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Country",
                }
            ),

            "bio": forms.TextInput(
               
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Bio",
                }
            ),

        }

# EducationFormSet = modelformset_factory(
#     Education, fields=('highest_qualification','specialization','institute','start_year','end_year'), extra=1
# )
class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['highest_qualification','specialization','institute','start_year','end_year']

        widgets = {
            "highest_qualification": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Highest qualification",
                }
            ),
            "specialization": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Specialization",
                }
            ),
            "institute": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Institute",
                }
            ),
            "start_year": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Start Year",
                }
            ),

            "end_year": forms.DateInput(
               
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "End Year",
                }
            ),

        }

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

        widgets = {
            "skill": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Skills",
                }
            ),
        
        }


class CertificationsForm(forms.ModelForm):
    class Meta:
        model = Certifications
        fields = ['certificate','issued_by','date_issued']

        widgets = {
            "certificate": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Certificate",
                }
            ),
            "issued_by": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Issued by",
                }
            ),
            "date_issued": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Date issued",
                }
            ),
      
        }


class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['title','link','desc']

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Title",
                }
            ),
            "link": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Link",
                }
            ),
            "desc": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Description",
                }
            ),
           
        }


        


        

        

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


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['highest_qualification','specialization','institute','institute_city', 'institute_state', 'institute_country','result','start_year','end_year','result']

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
            "institute_city": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Institute City",
                }
            ),
             "institute_state": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Institute State",
                }
            ),
             "institute_country": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Institute Country ",
                }
            ),
             "result": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "CGPA / Marks ",
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


class keyAchievementsForm(forms.ModelForm):
    class Meta:
        model = keyAchievements
        fields = ['achievement']

        widgets = {
            "achievement": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Key Achievements",
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


class LanguagesForm(forms.ModelForm):
    class Meta:
        model = Languages
        fields = ['language','proficiency_level']

        status_choices = (
            ("Elementary Proficiency",'Elementary Proficiency'),
            ("Limited Working Proficiency",'Limited Working Proficiency'),
            ("Professional Working Proficiency",'Professional Working Proficiency'), 
            ("Full Professional Proficiency",'Full Professional Proficiency'), 
            ("Native / Bilingual Proficiency",'Native / Bilingual Proficiency'), 
           
        )

        widgets = {
            "language": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Title",
                }
            ),
            "proficiency_level": forms.Select(
                choices=status_choices,
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Proficiency level",
                }
            ),
            
           
        }
        

        

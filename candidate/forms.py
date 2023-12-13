from django import forms
from .models import Candidate, Experience

class CandidateForm(forms.ModelForm):
    
    class Meta:
        model=Candidate
        fields=['skills','certificate_name','issued_by']
    def __init__(self, *args, **kwargs):
        super(CandidateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class DateInput(forms.DateInput):
    input_type = 'date'


class ExperienceForm(forms.ModelForm):

    class Meta:
        model = Experience
        fields = ['Designation','Organisation','status','descofjob','worked_from','worked_till']
        widgets = {
            'worked_from': DateInput(),
        }
        labels = {
            "Designation": "Designation",
            "Organisation": "Organisation",
            "Are You Currently Employeed": "status",
            "Job Description": "descofjob",
            "Worked from": "worked_from",
            "Worked Till": "worked_till",
            
        }
        
        
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
        

    
   
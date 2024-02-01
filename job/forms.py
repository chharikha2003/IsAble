from django import forms
from .models import Job
from employer.models import Employer
class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title','city','category','description']
    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class JobFilterForm(forms.Form):
    job_type = forms.ChoiceField(choices=[])
    sector = forms.ChoiceField(choices=[], required=False)
    city = forms.ChoiceField(choices=[], required=False)
    disability_type = forms.ChoiceField(choices=[], required=False)

    def __init__(self, *args, **kwargs):
        super(JobFilterForm, self).__init__(*args, **kwargs)
        self.fields['job_type'].choices = self.get_job_type_choices()
        self.fields['city'].choices = self.get_city_choices()
        self.fields['disability_type'].choices = self.get_disability_type_choices()
        self.fields['sector'].choices = self.get_sector_type_choices()


    def get_job_type_choices(self):
        # Retrieve the disability type choices from the model
        job_type = Employer._meta.get_field('sector').choices
        return job_type

    def get_city_choices(self):
        cities = Job._meta.get_field('city').choices
        return cities

    def get_disability_type_choices(self):
        # Retrieve the disability type choices from the model, handling possible None values
        disability_types = Job._meta.get_field('disability_type').choices
        return disability_types
   
    def get_sector_type_choices(self):
        # Retrieve the disability type choices from the model
        sectors = Employer._meta.get_field('industry_type').choices
        return sectors
   
        
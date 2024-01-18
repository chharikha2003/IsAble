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
    job_type = forms.ChoiceField(choices=[('private', 'Private'), ('government', 'Government')])
    sector = forms.ModelChoiceField(queryset=Employer.objects.values_list('sector', flat=True).distinct(), required=False)
    disability_type = forms.ModelChoiceField(queryset=Job.objects.values_list('disability_type', flat=True).distinct(), required=False)
    country = forms.ModelChoiceField(queryset=Job.objects.values_list('country', flat=True).distinct(), required=False)
    
   
        
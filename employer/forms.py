from django import forms
from .models import Employer
from accounts.validators import allow_only_images_validator
class Employerform(forms.ModelForm):
    company_license=forms.FileField(widget=forms.FileInput(attrs={'class':'btn btn-info'}),validators=[allow_only_images_validator])
    class Meta:
        model=Employer
        fields=['company_name','company_license']


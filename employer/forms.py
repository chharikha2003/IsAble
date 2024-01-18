from django import forms
from .models import Employer, Employer_Detailed
from accounts.validators import allow_only_images_validator
class Employerform(forms.ModelForm):
    company_license=forms.FileField(widget=forms.FileInput(attrs={'class':'btn btn-info'}),validators=[allow_only_images_validator])
    company_logo=forms.FileField(widget=forms.FileInput(attrs={'class':'btn btn-info'}),validators=[allow_only_images_validator])
    class Meta:
        model=Employer
        fields=['company_name','company_license','company_logo','company_desc','company_address','company_phone','company_website','twitter','linkedin','accessibility_features','support_services','inclusive_hiring_practices','sector','industry_type']
    def __init__(self, *args, **kwargs):
        super(Employerform, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

# class EmployerDetailsForm(forms.ModelForm):
#     logo=forms.FileField(widget=forms.FileInput(attrs={'class':'btn btn-info'}),validators=[allow_only_images_validator])
#     class Meta:
#         model =Employer_Detailed
#         fields = ['description','industry','founded_year','address','city','state','country','phone','website','logo','facebook','linkedin','twitter']


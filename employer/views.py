from django.shortcuts import render,redirect

from employer.forms import Employerform
from employer.models import Employer
from django.contrib.auth.decorators import login_required,user_passes_test
from django.core.exceptions import PermissionDenied

def check_role_candidate(user):
    if user.role==1:
        return True
    else:
        raise PermissionDenied
    
def check_role_employer(user):
    if user.role==2:
        return True
    else:
        raise PermissionDenied

@login_required(login_url='login')
@user_passes_test(check_role_employer)
def companyprofile_view(request):
    logged_in_user = request.user

    # Fetch the company details associated with the logged-in user
    company_details = Employer.objects.filter(user=logged_in_user)

    context = {
        'company_details': company_details
    }

    return render(request, 'employer/compprofile.html', context)
from django.shortcuts import render,redirect

from employer.forms import Employerform
from employer.models import Employer

# Create your views here.
# def companyregistration_view(request):
#     print("func called")
#     if request.method == 'POST':
#         employer_details_form =Employerform(request.POST,request.FILES)
        
#         print("yess")
#         if employer_details_form.is_valid():
#             # Save each form individually to the respective models
#             print('valid')
#             employer_details = employer_details_form.save(commit=False)
#             employer_details.user = request.user
            
#             employer_details.save()


#             print('savedd')
#             # Redirect or do something else
#             return redirect('employerDashboard')
#         else:
           
#             print(employer_details_form.errors)
           

#     else:
        
#         employer_form = Employerform()
       

        

#     return render(request, 'employer/compprofile.html', {'employer_form':employer_form})


def companyprofile_view(request):
    logged_in_user = request.user

    # Fetch the company details associated with the logged-in user
    company_details = Employer.objects.filter(user=logged_in_user)

    context = {
        'company_details': company_details
    }

    return render(request, 'employer/compprofile.html', context)
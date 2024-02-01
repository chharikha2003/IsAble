
# Create your views here.
# jobs/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from employer.models import Employer
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import Job
from .forms import JobFilterForm, JobForm
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
#job_list is a list of jobs posted by different companies
def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'job/job_list.html', {'jobs': jobs})

def job_detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'job/job_detail.html', {'job': job})
login_required(login_url='login')
@user_passes_test(check_role_employer)
def post_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            jobpost_save=form.save(commit=False)
            employer = Employer.objects.get(user=request.user)
            
            jobpost_save.company=employer
            
            form.save()
            return redirect('job_list')
    else:
        form = JobForm()
    return render(request, 'job/post_job.html', {'form': form})

def search_by_category(request):
    query=request.GET['query']
    jobs_by_cat=Job.objects.filter(category__icontains=query)
    return render(request,'job/search_by_category.html',{'jobs_by_cat':jobs_by_cat})
def search_by_city(request):
    query=request.GET['query1']
    jobs_by_city=Job.objects.filter(city__icontains=query)
    return render(request,'job/search_by_city.html',{'jobs_by_city':jobs_by_city})

def search_by_title(request):
    query=request.GET['query3']
    jobs_by_title=Job.objects.filter(title__icontains=query)
    return render(request,'job/search_by_title.html',{'jobs_by_title':jobs_by_title})


def get_internships(request):
    job = Job.objects.filter(category="Internship")
    return render(request, 'job/job_internship.html', {'job': job})
   
def get_remote(request):
    job = Job.objects.filter(category="Remote")
    return render(request, 'job/job_remote.html', {'job': job})
   


def get_fulltime(request):
    job = Job.objects.filter(category="Full Time")
    return render(request, 'job/job_fulltime.html', {'job': job})


# jobs/views.py
from django.shortcuts import render
from .models import Job
from .forms import JobFilterForm

def job_list(request):
    if request.method == 'POST':
        form = JobFilterForm(request.POST)
        if form.is_valid():
            job_type = form.cleaned_data.get('job_type')
            sector = form.cleaned_data.get('sector')
            city = form.cleaned_data.get('city')
            disability_type = form.cleaned_data.get('disability_type')

            # Apply filters based on form input
            jobs = Job.objects.all()

            if job_type != 'All':
                jobs = jobs.filter(company__sector=job_type)
                print(jobs)
            if sector != 'All':
                jobs = jobs.filter(company__industry_type=sector)
                print(jobs)

            if city != 'All':
                jobs = jobs.filter(city=city)
                print(jobs)
            if disability_type != 'All':
                jobs = jobs.filter(disability_type=disability_type)
                print(jobs)

            # Order by date_posted
            jobs = jobs.order_by('-date_posted')
    else:
        # If no form submission, set default values for the dropdowns to 'All'
        form = JobFilterForm(initial={'job_type': 'All', 'sector': 'All', 'city': 'All', 'disability_type': 'All'})
        
        # Display all jobs ordered by date_posted
        jobs = Job.objects.all().order_by('-date_posted')

    return render(request, 'job/job_list.html', {'form': form, 'jobs': jobs})

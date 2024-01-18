from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('job_filter/',views.job_filter,name='job_filter'),
    path('<int:job_id>/', views.job_detail, name='job_detail'),
    path('post/', views.post_job, name='post_job'),
   
    path('search_by_category',views.search_by_category,name='search_by_category'),
    path('search_by_city',views.search_by_city,name='search_by_city'),
    path('search_by_title',views.search_by_title,name='search_by_title'),
    path('get_internships',views.get_internships,name='get_internships'),
    path('get_remote',views.get_remote,name='get_remote'),
    path('get_fulltime',views.get_fulltime,name='get_fulltime'),

]
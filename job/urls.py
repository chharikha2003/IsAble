from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('<int:job_id>/', views.job_detail, name='job_detail'),
    path('post/', views.post_job, name='post_job'),
    path('search_by_category',views.search_by_category,name='search_by_category'),
    path('search_by_city',views.search_by_city,name='search_by_city'),
    path('search_by_title',views.search_by_title,name='search_by_title'),

]
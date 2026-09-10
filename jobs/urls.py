from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('jobs/<int:pk>/', views.job_detail, name='job_detail'),
    path('jobs/<int:pk>/apply/', views.apply, name='apply'),
    path('applications/', views.my_applications, name='my_applications'),
    path('recruiter/jobs/', views.recruiter_jobs, name='recruiter_jobs'),
    path('recruiter/jobs/new/', views.create_job, name='create_job'),
    path('recruiter/jobs/<int:pk>/applications/', views.manage_applications, name='manage_applications'),
]

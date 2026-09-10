from django.urls import path
from .api import ApplicationListCreateAPIView, JobDetailAPIView, JobListCreateAPIView

urlpatterns = [
    path('jobs/', JobListCreateAPIView.as_view(), name='api_job_list'),
    path('jobs/<int:pk>/', JobDetailAPIView.as_view(), name='api_job_detail'),
    path('applications/', ApplicationListCreateAPIView.as_view(), name='api_application_list'),
]

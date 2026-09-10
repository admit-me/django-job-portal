from rest_framework import serializers
from .models import Application, Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'title', 'company', 'location', 'description', 'skills', 'job_type', 'salary', 'recruiter', 'created_at', 'is_active']
        read_only_fields = ['recruiter', 'created_at']


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'job', 'candidate', 'resume_url', 'cover_letter', 'status', 'created_at']
        read_only_fields = ['candidate', 'status', 'created_at']

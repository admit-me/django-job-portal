from django.conf import settings
from django.db import models

class Job(models.Model):
    JOB_TYPES=[('FULL_TIME','Full Time'),('PART_TIME','Part Time'),('INTERNSHIP','Internship')]
    title=models.CharField(max_length=200)
    company=models.CharField(max_length=200)
    location=models.CharField(max_length=120)
    description=models.TextField()
    skills=models.CharField(max_length=500,help_text='Comma-separated skills')
    job_type=models.CharField(max_length=20,choices=JOB_TYPES,default='FULL_TIME')
    salary=models.CharField(max_length=100,blank=True)
    recruiter=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='posted_jobs')
    created_at=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)
    def __str__(self): return f'{self.title} - {self.company}'

class Application(models.Model):
    STATUS=[('APPLIED','Applied'),('SHORTLISTED','Shortlisted'),('REJECTED','Rejected'),('HIRED','Hired')]
    job=models.ForeignKey(Job,on_delete=models.CASCADE,related_name='applications')
    candidate=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='applications')
    resume_url=models.URLField(blank=True)
    cover_letter=models.TextField(blank=True)
    status=models.CharField(max_length=20,choices=STATUS,default='APPLIED')
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints=[models.UniqueConstraint(fields=['job','candidate'],name='unique_job_candidate')]

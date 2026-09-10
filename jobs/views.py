from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect, render
from .models import Application, Job

def job_list(request):
    jobs=Job.objects.filter(is_active=True)
    q=request.GET.get('q','').strip()
    location=request.GET.get('location','').strip()
    if q: jobs=jobs.filter(title__icontains=q)
    if location: jobs=jobs.filter(location__icontains=location)
    return render(request,'jobs/job_list.html',{'jobs':jobs})

def job_detail(request,pk):
    return render(request,'jobs/job_detail.html',{'job':get_object_or_404(Job,pk=pk)})

@login_required
def apply(request,pk):
    job=get_object_or_404(Job,pk=pk,is_active=True)
    if request.method=='POST':
        try:
            Application.objects.create(job=job,candidate=request.user,resume_url=request.POST.get('resume_url',''),cover_letter=request.POST.get('cover_letter',''))
        except IntegrityError:
            pass
    return redirect('job_detail',pk=job.pk)

@login_required
def my_applications(request):
    apps=Application.objects.select_related('job').filter(candidate=request.user)
    return render(request,'jobs/applications.html',{'applications':apps})

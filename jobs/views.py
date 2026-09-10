from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ApplicationForm, JobForm
from .models import Application, Job


def job_list(request):
    jobs = Job.objects.filter(is_active=True).order_by('-created_at')
    q = request.GET.get('q', '').strip()
    location = request.GET.get('location', '').strip()
    job_type = request.GET.get('job_type', '').strip()
    if q:
        jobs = jobs.filter(title__icontains=q) | jobs.filter(skills__icontains=q) | jobs.filter(company__icontains=q)
    if location:
        jobs = jobs.filter(location__icontains=location)
    if job_type:
        jobs = jobs.filter(job_type=job_type)
    return render(request, 'jobs/job_list.html', {'jobs': jobs, 'job_types': Job.JOB_TYPES})


def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    already_applied = request.user.is_authenticated and Application.objects.filter(job=job, candidate=request.user).exists()
    return render(request, 'jobs/job_detail.html', {'job': job, 'already_applied': already_applied, 'form': ApplicationForm()})


@login_required
def apply(request, pk):
    job = get_object_or_404(Job, pk=pk, is_active=True)
    if request.method != 'POST':
        return redirect('job_detail', pk=job.pk)
    if Application.objects.filter(job=job, candidate=request.user).exists():
        messages.info(request, 'You have already applied for this job.')
        return redirect('job_detail', pk=job.pk)
    form = ApplicationForm(request.POST)
    if form.is_valid():
        application = form.save(commit=False)
        application.job = job
        application.candidate = request.user
        application.save()
        messages.success(request, 'Application submitted successfully.')
    return redirect('job_detail', pk=job.pk)


@login_required
def my_applications(request):
    applications = Application.objects.select_related('job').filter(candidate=request.user).order_by('-created_at')
    return render(request, 'jobs/applications.html', {'applications': applications, 'page_title': 'My Applications'})


@login_required
def recruiter_jobs(request):
    jobs = Job.objects.filter(recruiter=request.user).order_by('-created_at')
    return render(request, 'jobs/recruiter_jobs.html', {'jobs': jobs})


@login_required
def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.recruiter = request.user
            job.save()
            messages.success(request, 'Job posted successfully.')
            return redirect('recruiter_jobs')
    else:
        form = JobForm()
    return render(request, 'jobs/job_form.html', {'form': form, 'page_title': 'Post a Job'})


@login_required
def manage_applications(request, pk):
    job = get_object_or_404(Job, pk=pk, recruiter=request.user)
    applications = job.applications.select_related('candidate').order_by('-created_at')
    if request.method == 'POST':
        application = get_object_or_404(Application, pk=request.POST.get('application_id'), job=job)
        status = request.POST.get('status')
        valid_statuses = {value for value, _ in Application.STATUS}
        if status in valid_statuses:
            application.status = status
            application.save(update_fields=['status'])
            messages.success(request, 'Application status updated.')
        return redirect('manage_applications', pk=job.pk)
    return render(request, 'jobs/manage_applications.html', {'job': job, 'applications': applications, 'statuses': Application.STATUS})

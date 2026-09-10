from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Application, Job

User = get_user_model()


class JobPortalTests(TestCase):
    def setUp(self):
        self.recruiter = User.objects.create_user(username='recruiter', password='testpass123')
        self.candidate = User.objects.create_user(username='candidate', password='testpass123')
        self.job = Job.objects.create(
            title='Python Developer', company='Example Tech', location='Hyderabad',
            description='Build Django applications.', skills='Python, Django, SQL', recruiter=self.recruiter
        )

    def test_job_list_shows_active_jobs(self):
        response = self.client.get(reverse('job_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Python Developer')

    def test_candidate_can_apply_once(self):
        self.client.login(username='candidate', password='testpass123')
        response = self.client.post(reverse('apply', args=[self.job.pk]), {'resume_url': 'https://example.com/resume', 'cover_letter': 'I am interested.'})
        self.assertRedirects(response, reverse('job_detail', args=[self.job.pk]))
        self.assertEqual(Application.objects.count(), 1)
        self.client.post(reverse('apply', args=[self.job.pk]), {})
        self.assertEqual(Application.objects.count(), 1)

    def test_recruiter_can_post_job(self):
        self.client.login(username='recruiter', password='testpass123')
        response = self.client.post(reverse('create_job'), {
            'title': 'Django Engineer', 'company': 'Acme', 'location': 'Remote',
            'description': 'Develop APIs.', 'skills': 'Django, DRF', 'job_type': 'FULL_TIME', 'salary': '6 LPA'
        })
        self.assertRedirects(response, reverse('recruiter_jobs'))
        self.assertEqual(Job.objects.filter(recruiter=self.recruiter).count(), 2)

    def test_recruiter_cannot_manage_another_recruiters_job(self):
        other = User.objects.create_user(username='other', password='testpass123')
        self.client.login(username='other', password='testpass123')
        response = self.client.get(reverse('manage_applications', args=[self.job.pk]))
        self.assertEqual(response.status_code, 404)

from django import forms
from .models import Application, Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'location', 'description', 'skills', 'job_type', 'salary']
        widgets = {'description': forms.Textarea(attrs={'rows': 6}), 'skills': forms.TextInput(attrs={'placeholder': 'Python, Django, SQL'})}


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['resume_url', 'cover_letter']
        widgets = {'cover_letter': forms.Textarea(attrs={'rows': 6})}

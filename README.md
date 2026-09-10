# Django Job Portal

A portfolio-ready full-stack recruitment platform built with **Python, Django and Django REST Framework**. It demonstrates authentication, job discovery, recruiter workflows, candidate applications, database relationships, permissions and automated testing.

## Features

### Candidates
- Browse active jobs
- Search by title, company or skill
- Filter by location and job type
- Apply with resume URL and cover letter
- Prevent duplicate applications
- Track application status

### Recruiters
- Post jobs
- View jobs they created
- Review applications
- Update application status: Applied, Shortlisted, Rejected or Hired
- Access is restricted to their own job postings

### Engineering
- Django ORM and relational database design
- Django authentication and CSRF protection
- Django REST Framework API
- Database migration
- Automated unit tests
- GitHub Actions CI
- Environment-based configuration

## REST API

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/jobs/` | List active jobs |
| POST | `/api/jobs/` | Create a job (authenticated) |
| GET | `/api/jobs/<id>/` | View a job |
| GET | `/api/applications/` | View your applications |
| POST | `/api/applications/` | Submit an application |

## Tech Stack

- Python 3.11+
- Django 5
- Django REST Framework
- SQLite for development
- HTML/CSS
- GitHub Actions

## Run Locally

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
# source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/` and use `/admin/` for administration.

## Testing

```bash
python manage.py test
python manage.py check
```

## Project Structure

```text
django-job-portal/
├── config/
├── jobs/
│   ├── migrations/
│   ├── api.py
│   ├── api_urls.py
│   ├── forms.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── templates/
├── .github/workflows/ci.yml
├── manage.py
└── requirements.txt
```

## Portfolio Note

This project is designed as an interview-ready demonstration of practical Django development, including models, forms, authentication, permissions, REST APIs, testing and CI.

## Author

**Meka Praveen Kumar Reddy**  
Python / Django Developer

# Django Job Portal

> Full-stack recruitment platform built with Python, Django and Django REST Framework.

A portfolio project demonstrating practical backend development through candidate and recruiter workflows, authentication, permissions, relational data modeling, REST APIs, automated testing and CI.

## Key Features

### Candidate
- Browse active jobs
- Search by title, company or skill
- Filter by location and job type
- Submit applications with resume URL and cover letter
- Prevent duplicate applications
- Track application status

### Recruiter
- Create and manage job postings
- Review applications for owned jobs
- Update application status: Applied, Shortlisted, Rejected or Hired
- Restrict access to authorized job owners

### Engineering
- Django ORM and relational database design
- Authentication and CSRF protection
- Role-aware permissions
- Django REST Framework API
- Database migrations
- Automated unit tests
- GitHub Actions CI
- Environment-based configuration

## REST API

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/jobs/` | List active jobs |
| POST | `/api/jobs/` | Create a job (authenticated) |
| GET | `/api/jobs/<id>/` | Retrieve a job |
| GET | `/api/applications/` | View current user's applications |
| POST | `/api/applications/` | Submit an application |

## Tech Stack

**Python 3.11+ • Django 5 • Django REST Framework • SQLite • HTML/CSS • GitHub Actions**

## Run Locally

```bash
python -m venv venv
venv\Scripts\activate
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

## Skills Demonstrated

**Python • Django • Django REST Framework • REST APIs • ORM • Authentication • Authorization • Database Design • Testing • Git • GitHub Actions • Full-Stack Web Development**

## Author

**Meka Praveen Kumar Reddy**  
Python / Django Developer

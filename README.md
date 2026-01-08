# Django User Management REST API

A backend REST API built using Django and Django REST Framework that provides
CRUD operations for managing users with token-based authentication.

## Features
- User CRUD (Create, Read, Update, Delete)
- Token-based authentication
- Django ORM for database operations
- Proper HTTP status codes
- Django Admin integration

## Tech Stack
- Python
- Django
- Django REST Framework
- SQLite (development)

## API Endpoints
- GET /users/ – List users
- POST /users/ – Create user
- GET /users/{id}/ – Retrieve user
- PUT /users/{id}/ – Update user
- DELETE /users/{id}/ – Delete user

## Setup Instructions
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

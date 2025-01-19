# Task and Project Management API

## Overview
This project provides a RESTful API for managing projects, tasks, and comments. It allows users to create, retrieve, update, and delete projects, tasks, and comments with secure authentication.

## Features
- User authentication using JWT.
- CRUD operations for Projects, Tasks, and Comments.
- Task creation, updates, and status tracking
- Comments on tasks for collaboration
- RESTful API endpoints for easy integration with web and mobile applications

---

## Installation and Setup

### Prerequisites
1. Python (>=3.8)
2. pip (Python package manager)
3. Git

### Steps to Set Up Locally

1. **Clone the repository:**
    ```bash
    git clone https://github.com/s-nishad/project_management
    cd project_management
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/MacOS
    venv\Scripts\activate   # Windows
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**
    In Django settings.py, config for JWT, Rest Framework and others.

    ```bash
    AUTH_USER_MODEL = 'users.User'
   
    REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
   }
   
   SIMPLE_JWT = {
       'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
       'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
       'ROTATE_REFRESH_TOKENS': True,
       'BLACKLIST_AFTER_ROTATION': True,
       'ALGORITHM': 'HS256',
       'SIGNING_KEY': SECRET_KEY,
       'AUTH_HEADER_TYPES': ('Bearer',),
   }
    ```

5. **Apply migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7. **Access the application:**
    Open your browser and go to `http://127.0.0.1:8000/`.

---

## API Documentation

### Authentication Endpoints

1. **Register**
    - URL: `/api/users/register/`
    - Method: `POST`
    - Payload:
      ```json
      {
          "username": "nishad",
          "email": "nishad0788@gmail.com",
          "password": "password123",
          "first_name": "Shohanur",
          "last_name": "Nishad"
      }
      ```

2. **Login**
    - URL: `/api/users/login/`
    - Method: `POST`
    - Payload:
      ```json
      {
          "username": "nishad",
          "password": "password123"
      }
      ```
    - Response:
      ```json
      {
          "refresh": "<token>",
          "access": "<token>"
      }
      ```

---

### Project Endpoints

1. **List Projects**
    - URL: `/api/projects/`
    - Method: `GET`

2. **Create Project**
    - URL: `/api/projects/`
    - Method: `POST`
    - Payload:
      ```json
      {
          "name": "New Project",
          "description": "A sample project."
      }
      ```

3. **Retrieve Project**
    - URL: `/api/projects/{id}/`
    - Method: `GET`

4. **Update Project**
    - URL: `/api/projects/{id}/`
    - Method: `PUT/PATCH`
    - Payload:
      ```json
      {
          "name": "Updated Project Name",
          "description": "Updated project description."
      }
      ```

5. **Delete Project**
    - URL: `/api/projects/{id}/`
    - Method: `DELETE`

---

### Task Endpoints

1. **List Tasks**
    - URL: `/api/projects/{project_id}/tasks/`
    - Method: `GET`

2. **Create Task**
    - URL: `/api/projects/{project_id}/tasks/`
    - Method: `POST`
    - Payload:
      ```json
      {
          "title": "Task 1",
          "description": "This is the first task.",
          "status": "To Do",
          "priority": "High",
          "due_date": "2025-02-01T12:00:00Z"
      }
      ```

3. **Retrieve Task**
    - URL: `/api/tasks/{id}/`
    - Method: `GET`

4. **Update Task**
    - URL: `/api/tasks/{id}/`
    - Method: `PUT/PATCH`
    - Payload:
      ```json
      {
          "title": "Updated Task",
          "status": "In Progress"
      }
      ```

5. **Delete Task**
    - URL: `/api/tasks/{id}/`
    - Method: `DELETE`

---

### Comment Endpoints

1. **List Comments**
    - URL: `/api/comments/{task_id}/`
    - Method: `GET`

2. **Create Comment**
    - URL: `/api/comments/{task_id}/`
    - Method: `POST`
    - Payload:
      ```json
      {
          "content": "This is a comment."
      }
      ```

---

## config settings.py for swagger
I have used here drf-spectacular
```bash
SPECTACULAR_SETTINGS = {
    'TITLE': 'Project Management',
    'DESCRIPTION': 'API documentation for the Project Management System',
    'VERSION': '1.0.0',
    'ALLOWED_HOSTS': ALLOWED_HOSTS,
    'SCHEMA_PATH_PREFIX': '/api/',
    'SERVE_INCLUDE_SCHEMA': False,
}
```

---

## Additional Notes
- Here I have used sqlite3 database 
- Use the `access` token returned after login for authentication in subsequent requests. Include it as a header:
  ```http
  Authorization: Bearer <access_token>
  
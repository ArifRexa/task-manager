# Task Manager Web Application

This is a task management web application built with Django that allows multiple users to create, view, update, and delete tasks. The application also provides a REST API for managing tasks. Below are the instructions on setting up, running the project, and additional details about the application.

## Table of Contents
- Setup
- Git Version Control
- Environment Variables
- Running the Project
- Documentation
- API Endpoints
- Final Steps
- Setup
- Git Version Control

# Setup
### Git Version Control
Clone the repository to your local machine using the following command:
```bash
git clone https://github.com/your-username/task-manager.git
```
### Environment Variables
Create a .env file in the project directory to store sensitive information such as Django secret key and database credentials. Here's an example of the .env file:
```bash
SECRET_KEY=your_django_secret_key
DEBUG=True
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432
```
### Running the Project
- Navigate to the project directory:
```bash
cd task-manager
```
- Create a virtual environment (optional but recommended):
```bash
python -m venv venv
```
- Activate the virtual environment:
```bash
venv\Scripts\activate
```
- Install dependencies:
```bash
pip install -r requirements.txt
```

- Apply migrations:
```bash
python manage.py migrate
```

- Create a superuser (admin) account (optional but recommended):
```bash
python manage.py createsuperuser
```

- Start the development server:
```bash
python manage.py runserver
```

# API Endpoints
### API Root
```bash
URL: /tasks/api/
```
### Get All Tasks and Task images
Endpoint:
```bash
URL: /tasks/api/tasks/
URL: /tasks/api/tasks-images/
```
Method: GET
Functionality:
This endpoint retrieves all tasks from the database.

### Get a Specific Task
Endpoint:
```bash
URL: tasks/api/tasks/{task_id}/
URL: tasks/api/tasks-images/{id}
```
Method: GET


### Create a New Task
Endpoint:
```bash
URL: tasks/api/tasks/
URL: tasks/api/tasks-images/
```
Method: POST

Required Parameters:
title (string): Title of the task.
description (string): Description of the task.
due_date (string, format: "YYYY-MM-DD"): Due date of the task.
priority (string, options: "low", "medium", "high"): Priority level of the task.


### Update an Existing Task
Endpoint:
```bash
URL: tasks/api/tasks/{task_id}/
URL: tasks/api/tasks-images/{id}
```
Method: PUT or PATCH
Required Parameters:
title (string): Updated title of the task.
description (string): Updated description of the task.
due_date (string, format: "YYYY-MM-DD"): Updated due date of the task.
priority (string, options: "low", "medium", "high"): Updated priority level of the task.

### Delete a Task
Endpoint:
```bash
URL: tasks/api/tasks/{task_id}/
URL: tasks/api/tasks-images/{id}
```
Method: DELETE
Functionality:
This endpoint deletes the task identified by its task_id.

Expected Response:
HTTP Status Code: 204 No Content

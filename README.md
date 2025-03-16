# Individual_Python

FastAPI Task Manager

A simple CRUD API built with FastAPI and SQLite to manage tasks. This project demonstrates how to create and manage tasks using FastAPI, SQLAlchemy, and SQLite.

Features:

- CRUD Operations (Create, Read, Update, Delete)
- SQLite Database with SQLAlchemy ORM
- FastAPI for High Performance
- Swagger UI & ReDoc API Documentation
- Automatic Request Validation using Pydantic

📂 Project Structure

📁 Individual_Python/
│── main.py # FastAPI Application with CRUD Endpoints
│── database.py # Database Configuration with SQLAlchemy
│── models.py # Pydantic Models & SQLAlchemy ORM Models
│── test_api.py # API Testing Script using requests
│── requirements.txt # Project Dependencies
│── README.md # Project Documentation
│── .gitignore # Ignoring Unnecessary Files (e.g., **pycache**, tasks.db)

Getting Started

1. Clone the Repository

git clone https://github.com/mayyavalieva/Individual_Python.git
cd Individual_Python

2. Set Up a Virtual Environment

python -m venv venv
source venv/bin/activate # Mac/Linux
venv\Scripts\activate # Windows

3. Install Dependencies

pip install -r requirements.txt

4. Run the FastAPI Server

uvicorn main:app --reload

    •	Open Swagger UI → http://127.0.0.1:8000/docs
    •	Open ReDoc UI → http://127.0.0.1:8000/redoc

API Endpoints:

Method Endpoint Description
GET /tasks Get all tasks
GET /tasks/{task_id} Get a specific task
POST /tasks Create a new task
PUT /tasks/{task_id} Update a task
DELETE /tasks/{task_id} Delete a task

Example Task JSON:

{
"title": "Learn FastAPI",
"description": "Complete FastAPI project",
"completed": false
}

Running Tests:

You can test the API using HTTPie or cURL.

Test API Using HTTPie

http GET http://127.0.0.1:8000/tasks
http POST http://127.0.0.1:8000/tasks title="New Task" description="Testing" completed=false
http PUT http://127.0.0.1:8000/tasks/1 completed=true
http DELETE http://127.0.0.1:8000/tasks/1

Test API Using Python Script

python test_api.py

Tech Stack:
• FastAPI - High-performance Python web framework
• SQLAlchemy - ORM for database management
• SQLite - Lightweight SQL database
• Pydantic - Data validation and serialization
• Uvicorn - ASGI server

License:

This project is licensed under the MIT License.

Author:

Mayya Valieva

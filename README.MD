# Recipe Management Web App

## Introduction
This Django-based web application allows users to manage their favorite recipes. Users can create, update, and delete recipes, as well as search for specific recipes by name. The application also includes user registration and authentication features.

## Features
- User Registration and Login
- Recipe Management (Create, Update, Delete)
- Search Recipes by Name
- User Authentication and Authorization

## Prerequisites
- Python (3.7+)
- Django (3.0+)
- Django's built-in SQLite database (for development)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Anirudhrarao/RecipeBox.git
   cd recipe-management

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate

3. Install project dependencies:
    ```bash
    pip install -r requirements.txt

4. Run migrations:
    ```bash
    python manage.py migrate

5. python manage.py createsuperuser
    ```bash
    python manage.py createsuperuser 

6. Start the development server:
    ```bash
    python manage.py runserver

## Usage
- Access the admin interface by visiting http://127.0.0.1:8000/admin/ and log in with your superuser credentials.
- Use the main application at http://127.0.0.1:8000/ to manage recipes and register/login as a user.

## Screenshots

![Image Alt Text](https://images.unsplash.com/photo-1499744937866-d7e566a20a61?auto=format&fit=crop&q=80&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&w=2070)

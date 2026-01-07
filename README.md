# LibraryProject

This is a Django project created for the ALX Django Learn Lab.

## Project Overview

This project introduces Django development and demonstrates:
- Creating a Django project
- Running the development server
- Using the Django admin interface
- Managing a Book model

## Setup Instructions

1. Install Django:
   pip install django

2. Run database migrations:
   python manage.py migrate

3. Create a superuser:
   python manage.py createsuperuser

4. Start the development server:
   python manage.py runserver

5. Open the browser and visit:
   http://127.0.0.1:8000/admin/

## Admin Features

- Book model registered in admin
- Displays title, author, and publication year
- Search enabled by title and author
- Filters by author and publication year


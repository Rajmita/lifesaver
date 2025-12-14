# LifeSaver – Blood Donation Platform

## Overview
LifeSaver is a beginner-friendly web application built with Django that connects people in need of blood with potential donors. The platform helps save lives by making blood donation requests easy to create, view, and act upon.

## Who Can Post
- People who **need blood** can create a post with:
  - Name
  - Blood type
  - City
  - Contact number
  - Message / details
- Donors can view these posts and **contact the requester directly**.

## Features
- Create blood request posts.
- Display posts with:
  - Urgent badges
  - Verified contact badges
  - City location linked to Google Maps
  - Call and Copy contact buttons
- Delete your own posts easily from the frontend.
- Inspirational About page.
- Bootstrap-based clean and responsive UI.

## How It Works
1. Visit the website.
2. Add a blood donation request using the “Add Post” form.
3. The post appears on the home page for all users to see.
4. Donors can view details and contact the requester directly.
5. Requesters can delete their posts if needed.

## Tech Stack
- Python 3.12
- Django
- HTML, CSS, Bootstrap

## Usage
1. Clone the project.
2. Install requirements:  
   ```bash
   pip install django

## How to Run Locally
1. Open terminal / PowerShell in the project folder.  
2. Install Django (if not installed): pip install django
3. Run the server: python manage.py runserver
4. Open browser at http://127.0.0.1:8000/

## Optional: Create a superuser to manage all posts: 
   python manage.py createsuperuser






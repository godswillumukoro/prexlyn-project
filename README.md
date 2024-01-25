# Prexlyn Properties

A comprehensive real estate listing platform

![prexlyn screeenshot](prexlyn/static/images/readme/prexlyn-screenshot.png)

## Features
1. Create, Read, Update, and Delete Property Listings
2. User Authentication
3. Full search functionality
4. Customized Admin Dashboard

## Technology Stack
- Python
- Django
- PostgreSQL
- JavaScript
- HTML
- CSS

## Project Files Description

### Directories
- accounts: Authentication app
- listings: Listings app
- media: - Media uploads from the database
- pages: control views for `index`, `about`, and `contact` pages.
- prexlyn: contains `static` files and contains URL patterns for `accounts`, `listings`, and `admin` views
- realtors: Realtors app
- static: contains migrated `static` files from `prexlyn` directory for deployment purposes
- templates: HTML templates and partials

### Files
- manage.py: Command Line Utility that manages this django project
- requirements.txt: All installed python packages

## Getting Started
### 1. Clone this repository
`git clone <repository_url>`

### 2. Create a virtual environment: python -m venv venv
`python -m venv venv`

### 3. Activate the Virtual Environment
Windows: `venv\Scripts\activate`

MacOS or Unix: `source venv/bin/activate`

### 4. Install Required Packages
`pip install -r requirements.txt`

### 5. Apply Migrations
`python manage.py makemigrations`

`python manage.py migrate`

### 6. Run Development Server
`python manage.py runserver`

### 7. Accessing Development Server
Navigate to your web browser and enter the following URL: `http://127.0.0.1:8000/`

### 7. Accessing Admin Dashboard
Navigate to your web browser and enter the following URL: `http://127.0.0.1:8000/admin`

Now, you should have the project up and running locally. Feel free to explore and make any necessary adjustments based on your requirements.

## Visual WalkThrough
Play the video demo below to enjoy a visual walkthrough of the app's features.

[![Play](https://img.youtube.com/vi/nhXdaz2eHGY/0.jpg)](https://www.youtube.com/watch?v=nhXdaz2eHGY)

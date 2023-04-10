Overview
This is a simple Django project that allows users to search for movies and paginate through the results. It includes a SQLite database with a few sample movies to get started.

Prerequisites
Python 3.10
Django 4
Installation
Clone the repository

Install the required packages with pip:
pip install -r requirements.txt

Run the migrations to set up the database:
python manage.py migrate

Load the sample data into the database:
python manage.py loaddata movies.json

Start the development server:
python manage.py runserver

Open a web browser and navigate to http://localhost:8000 to see the search page.

Usage
The search page allows users to search for movies by title and paginate through the results.

To search for a movie, enter the title into the search bar and click "Search". The results will be displayed on the same page, with up to 10 movies per page. Use the "Previous" and "Next" buttons to paginate through the results.








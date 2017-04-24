# django-feedback

### Introduction
A django web app that allows a user to login/signup and fill out a feedback form.
The feedback data should only be viewed by an admin/superuser who can then export the data to into a csv.  The required fields are; 

 1. Name (automatically loaded from user object) 
 2. Phone number (validation is key here)
 3. Neighbourhood - A drop down with a list of hoods
 4. Rating - Choice fields from 1 to 5
 5. Comments - text area field


  # Dependencies
 The app depends on multiple packages;

   1.**Django Framework**- A web framework for Python.
   2.**PostgreSQL 9.5**
   3.**Twitter Bootstrap v3 (css and Javascript)**

   # Installation and Setup

**To be able to get this project to your local machine**

```sh
$ git clone https://github.com/BethMwangi/django-feedback.git
$  pip install virtual env
$ . venv/bin/activate
$  cd django-feedback/
$ pip install -r requirements.txt


 ## To execute the demo run the commands

 ```sh
$ PYTHONPATH=../ python ./manage.py migrate
$ PYTHONPATH=../ python ./manage.py runserver

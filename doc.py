# STEP 1
# run: pipenv install django==2.1 (version 2.1) in terminal
# run: pipenv shell (to activate virtual environment)
# run: django-admin startproject vidly (vidly is the folder name). Remove the inner vidly file & delete the outter vidly file
# open manage.py then click python interpreter on bottom left
# change to the py interpreter with the virtual env name in terminal ( & C:/Users/DAVIES/.virtualenvs/django-TF6dU37Q/Scripts/python.exe c:/django/doc.py ). Run: print("hello")
# run: & C:/Users/DAVIES/.virtualenvs/django-TF6dU37Q/Scripts/python.exe c:/django/manage.py runserver <<==this normally is: python manage.py runserver
# click on the server address in terminal to open in browser

#STEP 2
# create another app(component) run: & C:/Users/DAVIES/.virtualenvs/django-TF6dU37Q/Scripts/python.exe c:/django/manage.py startapp movies

# STEP 3
# To create your first view go to views.py in movies folder
# Define a function called index, pass a param in the function called request
# Scroll up to the top of the file before render & import HttpResponse from django.http
# Then nest "return HttpResponse("Hello world")" under the index function code block
# Create a urls.py file into movies folder
# In it create a var called urlpatterns that contains an array 
# Scroll up to the top  of the file import path from django.urls
# In the array add path('') as root function
# in same file import views using: from . import views
# pass 2 more arguments to path('', views.index, name='index')
# Go back to urls.py file in vidly folder, & import another class called "include" beside the already imported path above in the same urls.py file
# Add: path('movies/', include('movies.urls')) under the existing path
# finally runserver 
# add /movies in the url to see the output

# STEP 4
# Now lets create the models for the app
# open models.py in the movies directory
# create a class: class Genre(models.Model):
# under Genre nest name var containing models.CharField(max_length=255)
# Then create another class: class Movie(models.Model):
# under Movie nest title = models.CharField(max_length=255)
#                  release_year = models.IntegerField()
#                  number_in_stock = models.IntegerField()
#                  daily_rate = models.FloatField()
#                  genre = models.ForeignKey(Genre, on_delete=models.CASCADE )  <ForeignKey is used to create a relationship btw db tables, on_delete=models.CASCADE means on deletion of the genre the movie should also be deleted>

# STEP 5 Storing our model in a db (MIGRATIONS)
# Install DB Browser for sqlite on your system (already have it)
# Open DB Browser & open/drag & drop the db.sqlite3 file from the GUI into DB Browser
# To migrate our Tables to the DB Browser sqlite, first register our movies app by:
# Open apps.py in movies folder, copy the class name that contains AppConfig as param
# Open settings.py in vidly folder, in the INSTALLED_APPS var add the path to MoviesConfig: 'movies.apps.MoviesConfig'
# Open the terminal and run migration: & C:/Users/DAVIES/.virtualenvs/django-TF6dU37Q/Scripts/python.exe c:/django/manage.py makemigrations  <<==this normally is: python manage.py makemigrations
# Open the newly cretaed migration file: 0001_initial.py & cross-check it the operations list is ok
# run: & C:/Users/DAVIES/.virtualenvs/django-TF6dU37Q/Scripts/python.exe c:/django/manage.py migrate  <<==this normally is: python manage.py migrate
# Now check the update made on DB Browser Sqlite & expand the movies & genre tables (in my case i had to reopen DB Broswer Sqlite, recopy & paste the db.sqlite3 file from the GUI)
# Then click Browse Data, in Table input field click django_migrations to see the list

# STEP 6 (Changing The Models)
# Lets say you want to add a field 
# Open models.py in movies folder, import timezone from django.utils
# adding a new attribute/field to the Movie class eg: date_created = models.DateTimeField(default=timezone.now)
# run: & C:/Users/DAVIES/.virtualenvs/django-TF6dU37Q/Scripts/python.exe c:/django/manage.py makemigrations
# run: & C:/Users/DAVIES/.virtualenvs/django-TF6dU37Q/Scripts/python.exe c:/django/manage.py migrate 
# Now check the update made on DB Browser Sqlite  (in my case i had to reopen DB Broswer Sqlite, recopy & paste the db.sqlite3 file from the GUI)
# BONUS: To know the EXACT sql statement used to create a table eg 0001_initial.py run:
#        & C:/Users/DAVIES/.virtualenvs/django-TF6dU37Q/Scripts/python.exe c:/django/manage.py sqlmigrate movies 0001      <<==this normally is: python manage.py sqlmigrate movies 0001 

# STEP 7 (Admin)
# Now we want to allow the staff/admin to populate the db with list of movies, so we need to create an admin panel for this
# run: & C:/Users/DAVIES/.virtualenvs/django-TF6dU37Q/Scripts/python.exe c:/django/manage.py runserver
# add "/admin" to the url in localhost:8000
# without closing the running terminal, open a new terminal window and run: & C:/Users/DAVIES/.virtualenvs/django-TF6dU37Q/Scripts/python.exe c:/django/manage.py createsuperuser     <<== this normally is: python manage.py createsuperuser 
# Enter user name, email, password, confirm password
# Go back to admin login page on localhost & login with the created details
# open admin.py file in movies folder
# import Genre, Movie from .models
# Type in: admin.site.register(Genre)
#          admin.site.register(Movie)
# Go back to the admin dashboard & refresh the page (in my case had to restart the server)
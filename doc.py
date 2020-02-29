# STEP 1
# run: pipenv install django==2.1 (version 2.1) in terminal
# run: pipenv shell (to activate virtual environment)
# run: django-admin startproject vidly (vidly is the folder name). Remove the inner vidly file & delete the outter vidly file
# open manage.py then click python interpreter on bottom left
# change to the py interpreter with the virtual env name in terminal ( & C:/Users/DAVIES/.virtualenvs/django-TF6dU37Q/Scripts/python.exe c:/django/doc.py ). Run: print("hello")
# run: & C:/Users/DAVIES/.virtualenvs/django-TF6dU37Q/Scripts/python.exe c:/django/manage.py runserver
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
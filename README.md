# django-REST-API-from-scratch

To further understand backend I'm following the this tutorial https://www.youtube.com/watch?v=i5JykvxUk_A

## Setup
* Create a virtual environment. The environment is where we will install all the dependency to run such as Django. This environment will be activated when we want to work on our project. Anytime we work on our project we want to activate the environment.
* After creating the environment we'll install the dependencies

```bash
python3 -m venv .venv # create virtual environment

ls -a 

. .venv/bin/activate # command to active virtual environment

python3 --version # install python

pip3 install djangorestframework # tool to create REST API

django-admin # command list for django

django-admin startproject drinks .

python3 manage.py runserver
```

```bash
# leave the server running, in a new terminal tab
cd into working directory

python3 manage.py migrate
```

```bash
http://127.0.0.1:8000/admin # there's an admin portal, no user

python3 manage.py createsuperuser # follow prompts
    # username: admin 
    # email:
    # password: wasd
```

## models creation
```python
# create models.py file within app

from django.db import models # to inherit from a models class

# create model
```

```bash
python3 manage.py makemigrations drinks # specify app
    # results an error, new installed app 'drinks'
    # settings.py > INSTALLED_APPS > add drinks

    # tried again, no error but no changes detected, my 'models.py' was incorrectly named 'model.py'
python3 manage.py migrate # no specification interesting

# tables still won't show in /admin
# create admin.py within app. this file will register the different tables within the admin panel.
# creating superuser and admin.py are not necessary
```

## Adding model to admin site
```python
#admin.py

from django.contrib import admin
from .models import Drink # current directory, models file, import model(s)

admin.site.register(Drink)

# refresh server
```



/admin

create drink objects

name for object is generic. we can change that within model.py. it's called the representation:

```python
# models.py

def __str__(self):
    # return representation
```

## Install framework within our INSTALLED_APPS
```python
# settings.py
# we've installed djangorestframework, but we need to install it to our app list

INSTALLED_APPS = [
    ...,
    'rest_framework',
    ...
]
```

## Serializers.py
```python
# create a serializers.py within app

# Create the DrinkSerializer class
```

## views.py
```python
# create views.py within drinks

# we are creating the following within this .py file:

# get all the drinks
# serialize them
# return json
```

# add to urls.py
```python
# now we need to say which url is going to hit the view > urls.py
# from drinks import views

# add a new path /drinks, have the request get the function within views

# visiting the site results in an error:
    # In order to allow non-dict objects to be serialized set the safe parameter to False
    # this is a setting that can be changed within views.py on the return JsonResponse

# after visiting the site we can see it's a list, if we want it as an object we can surround the
# serializer.data in a dictionary {}, which gives us our object
```

Great at this point you have a working api. Extremely limited it get only retrieve data. Meaning we've 1/4 of CRUD:
* Create
* Read (GET) -> this is us right now.
* Update
* Delete

## Extending views.py functionality
We're going to use a decorator in our drink_list() function. This decorator will let us describe the functionality in some way. The decorator will allow us to condition the request.method.

## Testing POST
We can use a tool like postman. [Postman](https://www.postman.com/downloads/) allows for api testing. We can switch our request to POST and in the body we can send data.
Change text to JSON and send through an request. Make sure it's only the name and description fields the id is assigned.

To see that the data made it to the database we call the GET request or /admin.

## Requesting information about one drink
First add to our urls.py a path specifying an id:

```python
path(f'drinks/<int:id>', views.drink_detail)
```

Create a new function drink_detail(). We're going to use a different method to return data. Currently in our drink_list() we're using `JsonResponse` and `Response`.
* `JsonResponse` is from the django.http library.
* `Response` is from the  django rest framework. This is the preferred way to return information.
* * We're going to work on setting response with some functionality that allows for better data browsing. We'll return JSON or HTML.

We can test via the API tool or the the browser.

## Re-adding the ability to get json data
We need to add the capability in our urls.py by adding a function to take different extensions.

```python
urlpatterns = format_suffix_patterns(urlpatterns)
```

# Consuming the api.
Very simple request via python to show how to consume the api. Create a consume.py file. Out side of drinks.
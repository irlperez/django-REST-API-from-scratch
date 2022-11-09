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
# create models.py file witin app

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

```python
# within admin.py

from django.contrib import admin
from .models import Drink # current directory, models file, import model(s)

admin.site.register(Drink)

# refresh server
```

```
/admin

create drink objects

name for object is generic. we can change that within model.py. it's called the representation.=
```

```python
# models.py

def __str__(self):
    # return representation
```

```python
# settings.py
# we've installed djangorestframework, but we need to install it to our app list

INSTALLED_APPS = [
    ...,
    'rest_framework',
    ...
]

# create a serializers.py within app

```
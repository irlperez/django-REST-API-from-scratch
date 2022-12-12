# to build: open the desktop app > then use the command 'docker build . -t django-dev' > 

# to run use the command 'docker run -it --rm django-dev'. '-it' is interactive mode. '--rm' deletes the container after stopping the container.

# to run using a port binding use the command 'docker run -p 8001:8000 -it --rm django-dev'. grabs all the connections from 8001 (host machine, docker) and binds to local host machine (8000, our computers). > to access we now use 8001 'http://127.0.0.1:8001/'


# any time we change the Dockerfile we need to build the image.



# docker comments must be indicated the beginning of a line.

# this is what our base image is going to run on.
FROM python:3

# enviorment variable that needs to be injected when we run python inside another process. this helps with seeing logs.
ENV PYTHONUNBUFFERED 1

# create working directory
RUN mkdir /code

# set the working directory
WORKDIR /code 

# copy the requirements.txt to the working directory
COPY requirements.txt /code/

# install the depencies. --user installs the package in a home directory that will most likey not require previlages.
RUN pip install --user -r requirements.txt

# copy the entire project to the code directory.
COPY . /code/

# this is the command we are telling Docker to run. It's technically considered JSON so we can't use single quotes.
# CMD python manage.py runserver """ OLD VERSION """"

# specify four 0s. this is for binding connections. when we don't know what ip address we want to run our server. along with port 8000.
CMD python manage.py runserver 0.0.0.0:8000 


### commands not working ###
# make sure docker app is open
# we can try reinstalling docker with: brew install --cask docker
# install docker via brew with 'brew install docker'
# install docker-compose with 'brew install docker-compose'
# install docker-machine with 'brew install docker-machine'
# `Dock`er
## What is docker?
Platform for developing, shipping, and running applications. Allows for separation of our application from our infrastructure. Reduce the delay between writing code and running it in production. 

Software development platform with virtualization technology that makes it easy to develop and deploy apps in neatly packaged virtual **containerized** environments. Our apps can run the same on an environment. 

The containers act like micro-computers that each have a specific job. The have their own isolated cpu, memory, and network resources. 

This means we can start, stop, restart each container without affecting the others. Examples of these jobs are:
* Mysql database
* NodeJS application 

### Why not use a VM?
VM's use hypervisor technology. This disk images are massive because they contain an entire OS. Docker is a better solution. Once again we run dependencies in a lightweight, isolated, VM like environment known as a container.

This environment can be copied to other machines in minutes. Which then allow us to run and test code like before.

## Platform
Docker provides the ability to package and run an application in a loosely isolated environment called a **container**. Docker provides tooling and a platform to manage the lifecycle of our containers:
* develop our application and its supporting components using containers.
* the container becomes the unit for distributing and testing our application.
* when we're ready, deploy our application into our production environment, as a container or an orchestrated service. this works the same whether our production environment is local data center, a cloud provider, or a hybrid of the two.

## What problems does Docker solve?
Missing or incorrect application dependencies such as libraries, interpreters, code/binaries, users.

## History lesson
Founded as DotCloud in '08 by Solomon Hykes in Paris. 

## How to use docker.
### High Level
Install > docker File > docker image > docker container.
* Docker file – Simple text document that describes how the Docker image will be built, blueprint.
* Docker image – read-only templates with instructions for creating a Docker container.
* Docker container – is a runnable instance of an image.

### Steps
These steps assume you have Python, PIP, Django, requirements.txt.
1. [Install docker](https://docs.docker.com/get-docker/)
2. Create a `.dockerignore` file in the root folder. This is important in bigger projects but may not be necessary with this smaller project.
3. Create a file called `Dockerfile`. This will allow docker to build the image it will execute on the Docker Machine we created. Think of this as instructions on how to build our container/image.
    1. Open the docker application.
    2. build the docker image
    3. run the docker image, which creates our container - it's important to know that the localhost address is for the **container** not our machine. We need to bind the connection in the container to the host machine.



### Sources
[Docker Docs](https://docs.docker.com/get-started/overview/)
[What is Docker in 5 minutes](https://www.youtube.com/watch?v=_dfLOzuIg2o)
[What problems does Docker solve?](https://www.youtube.com/watch?v=XYqp4e9uLDg)
[What is Docker? The spark for the container revolution](https://www.infoworld.com/article/3204171/what-is-docker-the-spark-for-the-container-revolution.html)
[Dockerizing a Python Django Web Application - Writing the Dockerfile](https://semaphoreci.com/community/tutorials/dockerizing-a-python-django-web-application)
[Django HOW TO run apps in a container using Docker ? [Simply Explained]](https://www.youtube.com/watch?v=UV55ehkX16A)
[- Setup Docker Compose](https://www.section.io/engineering-education/dockerized-django-application-with-github-actions/)












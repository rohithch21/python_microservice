Steps - 
- Created a new conda env mservice with python3.7.6
- Installed django and djangorestframework
- Create a basic django app
- In the Django project root directory, create Dockerfile, docker-compose.yml and requirements.txt
- Docker commands in Dockerfile - install python, env pythonunbufffered 1, provide workdir, install lib with pip, copy to app in workdir
- 



- Created cloudAMPQ account by linking it with github and email - rohithch16@gmail.com, TeamName = personalLemur
[https://customer.cloudamqp.com/instance]


# Current status - Data published from Django app but Data not getting persisted in amin app - flask server db. 
# Triggering python consumer.py manaually its working as expected
# [Optional]Finally try porting the entire docker setup to another system.

# Setup
- Setup

Admin app -> Products creation and view likes

Prerequisites
Anaconda env setup - C:\ProgramData\Anaconda3\Scripts\activate dev
To start the admin application server - 
	docker-compose up
[Optional] Open Docker Desktop to see Docker build logs

To access the database server running in admin Docker container 
Note - Ensure docker container is running
mysql -h localhost -P 33066 --protocol=tcp -u root -p
 -p to give password
-u = user root
In docker app runs in 8000 port number, laptop too it runs on 8000
8000:8000 mapping


To start the admin application server - 
	docker-compose up
[Optional] Open Docker Desktop to see Docker build logs

To access the database server running in admin Docker container 
Note - Ensure docker container is running
mysql -h localhost -P 33067 --protocol=tcp -u root -p
 -p to give password
-u = user root

Flask server running on port 5000 on system =, in docker container, port - 8001
Mapping 8001:5000

This is done in docker-compose.yaml file

----------------
In case of changes to the application, database or queue -> rebuld the container
Docker-compose build
To force fully creation of containers
Docker-compose up --force-recreate

Postman collection created - Py_MIcroservice

# Dockerfile with python

### Summary
This repo contains an basic dockerfile with [python](https://hub.docker.com/_/python) and some basic extensions like mysql and flask

#### Requirements.txt
Here you can add additional extensions which are requierd by python

#### Src Folder
Place all your python code in this directory

There is already some code in this directory which is an example of an Flask webserver which lets you sign up on the website. The data would be stored in a database.

#### dockerfile
This file will define the docker container image.

Run this to build the image for an container:

docker build `docker build -t <imagename> .`

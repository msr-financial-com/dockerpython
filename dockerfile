# set base image (host OS)
FROM python:3.8-slim

# set the working directroy in the container
WORKDIR /code

# copy the dependencies file to the workign directory
COPY requirements.txt . 

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the src directory to the working directory
COPY src/ .

# set environment variables
ENV host=localhost
ENV mysql_port=3306
ENV mysql_user=root
ENV mysql_password=root
ENV mysql_db=BucketList

# command to run on container start
CMD gunicorn --bind 0.0.0.0:5000 server2:app

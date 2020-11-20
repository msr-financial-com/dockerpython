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

# command to run on container start
CMD ["python", "server.py"] 
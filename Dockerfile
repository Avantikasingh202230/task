# Dockerfile 

# pull the official docker image
FROM python:3.9.6-buster

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
    && apt-get -y install netcat gcc \
    && apt-get clean

# install python dependencies
RUN pip3 install --upgrade pip
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# copy project
COPY . .
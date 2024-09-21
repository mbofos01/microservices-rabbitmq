# Use an official Python runtime as a parent image
FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1 

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install libraries
RUN pip install -r /app/requirements.txt

# Specify the command to run on container start
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0", "--debug" ]
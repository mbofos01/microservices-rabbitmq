# Use the official Python base image
FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1 

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the pika library
RUN pip install pika

# Specify the command to run on container start
ENTRYPOINT ["python", "/app/receiver.py"]

# Use an official Python runtime as a parent image
FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1 

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install pika for RabbitMQ communication
RUN pip install pika

# Specify the command to run on container start
ENTRYPOINT ["python", "/app/producer.py"]
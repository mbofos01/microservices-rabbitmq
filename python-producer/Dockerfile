# Use an official Python runtime as a parent image
FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1 

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install pika for RabbitMQ communication
RUN pip install pika
RUN pip install flask
RUN pip install flask-restx

# Specify the command to run on container start
# ENTRYPOINT ["python", "/app/producer.py"]
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0", "--debug" ]
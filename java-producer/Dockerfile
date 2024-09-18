# Use the official OpenJDK JDK image
FROM openjdk:11-jdk-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Download the RabbitMQ Java client library and SLF4J dependencies
RUN apt-get update && apt-get install -y wget && \
    wget https://repo1.maven.org/maven2/com/rabbitmq/amqp-client/5.12.0/amqp-client-5.12.0.jar && \
    wget https://repo1.maven.org/maven2/org/slf4j/slf4j-api/1.7.30/slf4j-api-1.7.30.jar && \
    wget https://repo1.maven.org/maven2/org/slf4j/slf4j-simple/1.7.30/slf4j-simple-1.7.30.jar

# Compile the Java file using JDK (javac) with all dependencies
RUN javac -cp .:amqp-client-5.12.0.jar:slf4j-api-1.7.30.jar:slf4j-simple-1.7.30.jar Send.java

# Run the Send class with all dependencies in the classpath
CMD ["java", "-cp", ".:amqp-client-5.12.0.jar:slf4j-api-1.7.30.jar:slf4j-simple-1.7.30.jar", "Send"]

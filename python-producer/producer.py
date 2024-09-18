import pika

def main():
    # Connect to RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()

    # Declare a queue
    channel.queue_declare(queue='some_queue')

    # Publish a message
    message = "Hello World from Python!"
    channel.basic_publish(exchange='', routing_key='some_queue', body=message)
    print(f" [x] Sent '{message}'")

    # Close the connection
    connection.close()

if __name__ == "__main__":
    main()

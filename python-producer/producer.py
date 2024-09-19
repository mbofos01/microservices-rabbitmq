import pika
import json

def main():
    # Connect to RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()

    # Declare a queue
    channel.queue_declare(queue='some_queue')

    # Publish a message
    # message = "/shared/mntn.jpg" #"Hello World from Python!".

    message = {
        'image_path': "/shared/mntn.jpg",
        'size': 800
    }


    channel.basic_publish(exchange='', routing_key='some_queue', body=json.dumps(message))
    print(f" [x] Sent '{message}'")

    # Close the connection
    connection.close()

if __name__ == "__main__":
    main()

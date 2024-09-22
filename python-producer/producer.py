import pika
import json

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()

# Declare a queue
channel.queue_declare(queue='some_queue')

def cut_image(path, size=400):
    message = {
        'image_path': path,
        'size': size
    }

    channel.basic_publish(exchange='', routing_key='some_queue', body=json.dumps(message))
    print(f" [x] Sent '{message}'")

# Close the connection 
# No  need to close the connection in the producer since server is running
# connection.close()

if __name__ == "__main__":
    cut_image(path="/shared/mntn.jpg", size=800)

import pika
import time
import json
from image_edit import save_image_center

TIMEOUT_SECONDS=10

def callback(ch, method, properties, body):
    message = json.loads(body)
    image_path = message['image_path']
    crop_width = int(message['size'])

    print(f" [Y] Received message: {image_path.upper()}")
    save_image_center(image_path, crop_width=crop_width)

# Retry logic in case RabbitMQ is not ready yet
while True:
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
        channel = connection.channel()
        channel.queue_declare(queue='some_queue')
        break  # If connection is successful, exit the loop
    except pika.exceptions.AMQPConnectionError:
        print(f"RabbitMQ not available yet, retrying in {TIMEOUT_SECONDS} seconds...")
        time.sleep(TIMEOUT_SECONDS)

# Update to the new pika API format
channel.basic_consume(queue='some_queue', on_message_callback=callback, auto_ack=True)

print("Waiting for messages. To exit press CTRL+C")
channel.start_consuming()

import pika
import time

TIMEOUT_SECONDS=10

def callback(ch, method, properties, body):
    print(f" [Y] Received message: {body.decode().upper()}")

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

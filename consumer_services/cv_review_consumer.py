import json

import pika
from rabbit_mq.rabbit_mq_channel import CV_REVIEW_RESULTS
from utils.config import RABBITMQ_HOST, RABBITMQ_PASS, RABBITMQ_PORT, RABBITMQ_USER


def cv_review_callback(ch, method, properties, body):
    data = json.loads(body)
    print("Received:", data)

    ch.basic_ack(delivery_tag=method.delivery_tag)


def cv_review_consume():
    credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=RABBITMQ_HOST,
            port=RABBITMQ_PORT,
            credentials=credentials
        )
    )
    channel = connection.channel()
    channel.queue_declare(queue=CV_REVIEW_RESULTS, durable=True)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(
        queue=CV_REVIEW_RESULTS,
        on_message_callback=cv_review_callback,
    )

    channel.start_consuming()

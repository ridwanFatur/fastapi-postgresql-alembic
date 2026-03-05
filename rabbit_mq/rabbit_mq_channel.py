from utils.config import RABBITMQ_HOST, RABBITMQ_PASS, RABBITMQ_PORT, RABBITMQ_USER
import pika

RABBITMQ_URL = f"amqp://{RABBITMQ_USER}:{RABBITMQ_PASS}@{RABBITMQ_HOST}:{RABBITMQ_PORT}/"


params = pika.URLParameters(RABBITMQ_URL)
connection = pika.BlockingConnection(params)
channel = connection.channel()

CV_REVIEW_TASKS = "cv_review_tasks"
CV_REVIEW_RESULTS = "cv_review_results"

channel.queue_declare(queue=CV_REVIEW_TASKS, durable=True)

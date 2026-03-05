from fastapi import APIRouter, Depends, BackgroundTasks
from fastapi import Depends
from sqlalchemy.orm import Session
from db.database import get_db
import pika
import json
from rabbit_mq.rabbit_mq_channel import CV_REVIEW_TASKS, channel
import time

router = APIRouter(
    prefix="/api/cv_review",
    tags=["user"],
)


def process_cv(file_uri: str):
    print("Processing CV:", file_uri)
    time.sleep(5)
    print(f"Task done")


@router.post("/")
def upload_cv(background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    file_uri = "example_file_uri"
    background_tasks.add_task(process_cv, file_uri)
    # channel.basic_publish(
    #     exchange='',
    #     routing_key=CV_REVIEW_TASKS,
    #     body=json.dumps({
    #         "file_uri": "file_uri_example",
    #         "user_id": 1
    #     }),
    #     properties=pika.BasicProperties(
    #         delivery_mode=2,
    #     )
    # )

    return {"test": "test"}

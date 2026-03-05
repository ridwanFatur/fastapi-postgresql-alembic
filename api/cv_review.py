from fastapi import APIRouter, Depends
from fastapi import Depends
from sqlalchemy.orm import Session
from db.database import get_db
import pika
import json
from rabbit_mq.rabbit_mq_channel import CV_REVIEW_TASKS, channel

router = APIRouter(
    prefix="/api/cv_review",
    tags=["user"],
)


@router.post("/")
def upload_cv(db: Session = Depends(get_db)):
    channel.basic_publish(
        exchange='',
        routing_key=CV_REVIEW_TASKS,
        body=json.dumps({
            "file_uri": "file_uri_example",
            "user_id": 1
        }),
        properties=pika.BasicProperties(
            delivery_mode=2,
        )
    )

    return {"test":"test"}

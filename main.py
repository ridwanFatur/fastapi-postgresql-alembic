from fastapi import FastAPI
from api import cv_review, user
from consumer_services.cv_review_consumer import cv_review_consume
from db.database import engine, Base
from contextlib import asynccontextmanager
import threading

Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    thread = threading.Thread(target=cv_review_consume, daemon=True)
    thread.start()
    print("Start Consuming")
    yield


app = FastAPI(
    title="CV Insight AI",
    version="1.0.0",
    redirect_slashes=False,
    lifespan=lifespan
)


@app.get("/")
async def root():
    return {"message": "App is Ready"}

app.include_router(user.router)
app.include_router(cv_review.router)

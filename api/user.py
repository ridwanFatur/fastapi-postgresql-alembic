from fastapi import APIRouter, Depends
from fastapi import Depends
from sqlalchemy.orm import Session
from db.database import get_db
from models.user import User
from pydantic import BaseModel

router = APIRouter(
    prefix="/api/user",
    tags=["user"],
)

class UserCreate(BaseModel):
    name: str
    email: str

@router.post("/")
def create_user(payload: UserCreate, db: Session = Depends(get_db)):
    user = User(name=payload.name, email=payload.email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
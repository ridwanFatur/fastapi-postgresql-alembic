from sqlalchemy import Column, Integer, String, Text
from db.database import Base

class CVFeedback(Base):
    __tablename__ = "cv_feedbacks"

    id = Column(Integer, primary_key=True, index=True)
    file_link = Column(String, nullable=False)
    feedback = Column(Text, nullable=True)
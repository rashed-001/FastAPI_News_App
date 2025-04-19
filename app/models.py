from sqlalchemy import Column, Integer, String, Text, DateTime
from .database import Base

class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(Text, nullable=True)
    url = Column(String, unique=True, nullable=False)
    published_at = Column(DateTime, nullable=False)
    source = Column(String, nullable=True)
    country = Column(String, nullable=True)
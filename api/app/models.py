from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base

class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    category = Column(String)
    url = Column(String, unique=True, nullable=False)
    published_at = Column(DateTime)

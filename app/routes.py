from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import NewsCreate
from app.crud import create_news

router = APIRouter()

@router.post("/news")
def add_news(news: NewsCreate, db: Session = Depends(get_db)):
    return create_news(db, news)

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import NewsCreate
from app.crud import create_news
from typing import List
from app.schemas import NewsResponse
from app.crud import get_all_news

router = APIRouter()

@router.post("/news", status_code=201)
def add_news(news: NewsCreate, db: Session = Depends(get_db)):
    return create_news(db, news)


@router.get("/news", response_model=List[NewsResponse])
def list_news(db: Session = Depends(get_db)):
    return get_all_news(db)
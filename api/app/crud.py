from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from app.models import News
from app.schemas import NewsCreate

def create_news(db: Session, news: NewsCreate):
    try:
        item = News(**news.dict())
        db.add(item)
        db.commit()
        db.refresh(item)
        return item

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="News already exists"
        )
    
def get_all_news(db: Session):
    return db.query(News).all()

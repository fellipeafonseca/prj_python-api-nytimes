from sqlalchemy.orm import Session
from app.models import News
from app.schemas import NewsCreate

def create_news(db: Session, news: NewsCreate):
    item = News(**news.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

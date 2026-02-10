from pydantic import BaseModel
from datetime import datetime

class NewsCreate(BaseModel):
    title: str
    category: str
    url: str
    published_at: datetime

class NewsResponse(NewsCreate):
    id: int

    class Config:
        from_attributes = True

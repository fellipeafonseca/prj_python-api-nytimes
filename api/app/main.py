from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.routes import router
from app.logger import setup_logging

setup_logging()

app = FastAPI(title="NYTimes News API")

Base.metadata.create_all(bind=engine)

app.include_router(router)

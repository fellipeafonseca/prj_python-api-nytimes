import os
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
from sqlalchemy.exc import OperationalError

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = None
MAX_RETRIES = 5
RETRY_DELAY = 3  # segundos

for attempt in range(MAX_RETRIES):
    try:
        engine = create_engine(DATABASE_URL)
        engine.connect()
        print("✅ Banco conectado com sucesso")
        break
    except OperationalError:
        print(f"⏳ Banco indisponível, tentativa {attempt + 1}/{MAX_RETRIES}")
        time.sleep(RETRY_DELAY)

if engine is None:
    raise RuntimeError("❌ Não foi possível conectar ao banco de dados")


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()






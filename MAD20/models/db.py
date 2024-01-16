from contextlib import contextmanager

from MAD20.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URL = f"{settings.DB_TYPE}://{settings.DB_USER}:{settings.DB_PASS}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True) 


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


get_db_ctx = contextmanager(get_db)

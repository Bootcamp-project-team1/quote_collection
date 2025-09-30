from sqlalchemy import create_engine
from app.core.config import settings
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(settings.sync_database_url, pool_pre_ping=True,)

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try :
        yield db
    finally:
        db.close()
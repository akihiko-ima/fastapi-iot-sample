from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from config import get_settings


SQLALCHEMY_DATABASE_URL = get_settings().sqlalchemy_database_url

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# データベースセッションの取得とクリーンアップ
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

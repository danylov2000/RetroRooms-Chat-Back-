import os
from dotenv import load_dotenv
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from app.models import Base

load_dotenv()

DB_PROVIDER = os.environ.get("DB_PROVIDER")

if DB_PROVIDER == "postgres":
    POSTGRES_USER = os.environ.get('POSTGRES_USER')
    POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
    POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
    POSTGRES_PORT = os.environ.get('POSTGRES_PORT')
    POSTGRES_DB = os.environ.get('POSTGRES_DB')
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

else:
    DATABASE_URL = f"sqlite:///database.db"

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
session = Session(bind=engine)

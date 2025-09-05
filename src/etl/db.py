import time
from pymongo import MongoClient
import psycopg2
from sqlalchemy import create_engine
from .config import MONGO_URI, MONGO_DB, POSTGRES_URI
from .logger import logger

def get_mongo():
    for attempt in range(10):
        try:
            client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=2000)
            db = client[MONGO_DB]
            db.command("ping")
            return db
        except Exception as e:
            logger.warning(f"Mongo not ready (attempt {attempt+1}/10): {e}")
            time.sleep(2)
    raise RuntimeError("MongoDB connection failed.")

def get_pg():
    for attempt in range(10):
        try:
            return psycopg2.connect(POSTGRES_URI)
        except Exception as e:
            logger.warning(f"Postgres not ready (attempt {attempt+1}/10): {e}")
            time.sleep(2)
    raise RuntimeError("PostgreSQL connection failed.")

def get_pg_engine():
    return create_engine(POSTGRES_URI)

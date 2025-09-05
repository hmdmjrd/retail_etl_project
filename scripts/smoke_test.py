from src.etl.db import get_mongo, get_pg
from src.etl.logger import logger

if __name__ == "__main__":
    pg = get_pg(); logger.info("Postgres OK"); pg.close()
    db = get_mongo(); logger.info(f"Mongo OK; collections: {db.list_collection_names()}")

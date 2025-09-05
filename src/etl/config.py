import os
from dotenv import load_dotenv
load_dotenv()

MONGO_URI   = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB    = os.getenv("MONGO_DB", "retail_db")
POSTGRES_URI= os.getenv("POSTGRES_URI","postgresql://postgres:postgres@localhost:5432/retail_warehouse")

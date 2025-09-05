import os
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME   = os.getenv("MONGO_DB", "retail_db")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

customers = [
  {"customer_id":"CUST1001","name":"Alice Johnson","email":"alice@example.com","signup_date":"2023-05-10","country":"USA"},
  {"customer_id":"CUST1002","name":"Bob Miller","email":"bob@example.com","signup_date":"2023-06-20","country":"Germany"}
]
products = [
  {"product_id":"PROD2001","name":"Wireless Mouse","category":"Electronics","price":25.99},
  {"product_id":"PROD2002","name":"Mechanical Keyboard","category":"Electronics","price":79.00}
]
orders = [
  {"order_id":"ORD3001","customer_id":"CUST1001","items":[{"product_id":"PROD2001","quantity":2},{"product_id":"PROD2002","quantity":1}],"order_date":"2023-07-15","status":"delivered"},
  {"order_id":"ORD3002","customer_id":"CUST1002","items":[{"product_id":"PROD2002","quantity":1}],"order_date":"2023-08-10","status":"delivered"}
]

for name, docs in [("customers", customers), ("products", products), ("orders", orders)]:
    db[name].delete_many({})
    db[name].insert_many(docs)

print("MongoDB seeded with sample data.")

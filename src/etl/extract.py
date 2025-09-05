from .db import get_mongo
from .logger import logger

def fetch_all():
    db = get_mongo()
    customers = list(db.customers.find({}, {"_id":0}))
    products  = list(db.products.find({}, {"_id":0}))
    orders    = list(db.orders.find({}, {"_id":0}))
    logger.info(f"Fetched: customers={len(customers)}, products={len(products)}, orders={len(orders)}")
    return customers, products, orders

from typing import List, Dict, Any
from pydantic import BaseModel
from .logger import logger

class OrderItem(BaseModel):
    product_id: str
    quantity: int

class Order(BaseModel):
    order_id: str
    customer_id: str
    items: List[OrderItem]
    order_date: str

def explode_orders_to_facts(orders: List[Dict[str, Any]], products: List[Dict[str, Any]]):
    price_map = {p["product_id"]: float(p["price"]) for p in products}
    facts = []
    for o in orders:
        order = Order.model_validate(o)  # اعتبارسنجی ساختار ورودی
        for it in order.items:
            price = price_map[it.product_id]
            facts.append({
                "order_id": order.order_id,
                "customer_id": order.customer_id,
                "product_id": it.product_id,
                "quantity": int(it.quantity),
                "total_amount": float(it.quantity) * price,
                "order_date": order.order_date,
            })
    logger.info(f"Built fact rows: {len(facts)}")
    return facts

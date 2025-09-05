from src.etl.transform import explode_orders_to_facts

def test_explode_orders_to_facts_basic():
    products=[{"product_id":"P1","price":10.0},{"product_id":"P2","price":2.5}]
    orders=[{
        "order_id":"O1","customer_id":"C1","order_date":"2024-01-01",
        "items":[{"product_id":"P1","quantity":3},{"product_id":"P2","quantity":4}]
    }]
    facts = explode_orders_to_facts(orders, products)
    assert len(facts)==2
    assert sum(f["total_amount"] for f in facts) == 40.0

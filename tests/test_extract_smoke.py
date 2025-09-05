from src.etl.extract import fetch_all

def test_extract_returns_data():
    customers, products, orders = fetch_all()
    assert len(customers) > 0
    assert len(products)  > 0
    assert len(orders)    > 0

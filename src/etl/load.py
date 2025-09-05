from psycopg2.extras import execute_batch
from .db import get_pg
from .logger import logger

def upsert_dimensions(customers, products):
    conn = get_pg()
    with conn, conn.cursor() as cur:
        execute_batch(cur, """
            INSERT INTO dim_customers (customer_id, name, email, country, signup_date)
            VALUES (%(customer_id)s, %(name)s, %(email)s, %(country)s, %(signup_date)s::date)
            ON CONFLICT (customer_id) DO UPDATE SET
                name=EXCLUDED.name,
                email=EXCLUDED.email,
                country=EXCLUDED.country,
                signup_date=EXCLUDED.signup_date
        """, customers)
        execute_batch(cur, """
            INSERT INTO dim_products (product_id, name, category, price)
            VALUES (%(product_id)s, %(name)s, %(category)s, %(price)s)
            ON CONFLICT (product_id) DO UPDATE SET
                name=EXCLUDED.name,
                category=EXCLUDED.category,
                price=EXCLUDED.price
        """, products)
    conn.close()
    logger.info("Dimensions upserted.")

def upsert_facts(facts):
    conn = get_pg()
    with conn, conn.cursor() as cur:
        execute_batch(cur, """
            INSERT INTO fact_sales (order_id, customer_id, product_id, quantity, total_amount, order_date)
            VALUES (%(order_id)s, %(customer_id)s, %(product_id)s, %(quantity)s, %(total_amount)s, %(order_date)s::date)
            ON CONFLICT (order_id, product_id) DO UPDATE SET
                quantity=EXCLUDED.quantity,
                total_amount=EXCLUDED.total_amount,
                order_date=EXCLUDED.order_date,
                customer_id=EXCLUDED.customer_id
        """, facts)
    conn.close()
    logger.info("Facts upserted.")

from src.etl.logger import logger
from src.etl.extract import fetch_all
from src.etl.transform import explode_orders_to_facts
from src.etl.load import upsert_dimensions, upsert_facts
from src.etl.reports import export_reports

def main():
    try:
        logger.info("ETL started")
        customers, products, orders = fetch_all()
        upsert_dimensions(customers, products)
        facts = explode_orders_to_facts(orders, products)
        upsert_facts(facts)
        export_reports()
        logger.info("ETL finished successfully")
    except Exception as e:
        logger.exception(f"ETL failed: {e}")
        raise

if __name__ == "__main__":
    main()

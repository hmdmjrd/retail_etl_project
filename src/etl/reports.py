import os
import pandas as pd
from .db import get_pg_engine
from .logger import logger

def export_reports():
    os.makedirs("outputs", exist_ok=True)
    engine = get_pg_engine()

    q1 = """
      SELECT dc.customer_id, dc.name, dc.email, SUM(fs.total_amount) AS revenue
      FROM fact_sales fs
      JOIN dim_customers dc ON fs.customer_id = dc.customer_id
      GROUP BY 1,2,3
      ORDER BY revenue DESC;
    """
    df = pd.read_sql(q1, engine)
    df.to_csv("outputs/customer_revenue.csv", index=False)

    q2 = """
      SELECT DATE_TRUNC('month', order_date) AS month, SUM(total_amount) AS revenue
      FROM fact_sales
      GROUP BY 1
      ORDER BY 1;
    """
    df2 = pd.read_sql(q2, engine)
    df2["month"] = pd.to_datetime(df2["month"]).dt.strftime("%Y-%m")
    df2.to_json("outputs/monthly_sales.json", orient="records", indent=2)

    logger.info("Reports exported to outputs/")

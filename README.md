ETL: MongoDB -> Python -> PostgreSQL + Reports (CSV/JSON)
docker compose up -d
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python seed_data.py
PYTHONPATH=. python run_etl.py
pytest -q

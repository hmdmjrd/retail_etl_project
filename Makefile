VENV=.venv
PY=source $(VENV)/bin/activate;

up:
\tdocker compose up -d

down:
\tdocker compose down

ps:
\tdocker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

seed:
\t$(PY) python seed_data.py

run:
\t$(PY) PYTHONPATH=. python run_etl.py

test:
\t$(PY) PYTHONPATH=. pytest -q

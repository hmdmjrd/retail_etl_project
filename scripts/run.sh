#!/usr/bin/env bash
set -e
source .venv/bin/activate
PYTHONPATH=. python run_etl.py

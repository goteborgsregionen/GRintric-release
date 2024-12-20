#!/bin/bash

# Add src to Python's path
export PYTHONPATH="$PYTHONPATH:/backend/src"

poetry install --no-root
poetry run python init_db.py
poetry run alembic upgrade head
poetry run start
pip install tests
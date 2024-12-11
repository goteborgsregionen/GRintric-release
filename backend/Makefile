# Name of the tmux session
SESSION_NAME := intric-backend

start:
	tmux new -s $(SESSION_NAME) -d 'source ../.venv/bin/activate; docker compose up -d; poetry run python init_db.py; poetry run start'

attach:
	tmux a -t $(SESSION_NAME)

stop:
	tmux kill-session -t $(SESSION_NAME)
	docker compose down

restart: stop start

build:
	docker compose build

migrate:
	poetry run python init_db.py

worker:
	poetry run arq src.instorage.worker.worker.WorkerSettings

logs:
	docker compose logs -f

test:
	poetry run pytest  # Or adjust the command for your testing framework

lint:
	poetry run pylint src  # Or adjust for your linter and code directory

fmt:
	poetry run black src  # Or adjust for your code formatter

# Add more targets as needed (e.g., for deployment, database backups, etc.)
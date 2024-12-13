# Define tmux session names
BACKEND_SESSION_NAME := intric-backend
FRONTEND_SESSION_NAME := intric-frontend

# Build all, then start both backend and frontend
build-all-start: backend-build frontend-build start

# Start both backend and frontend in detached tmux sessions
start:
	tmux new -s $(BACKEND_SESSION_NAME) -d 'source .venv/bin/activate; cd backend; docker compose up -d; poetry run python init_db.py; poetry run start'
	tmux new -s $(FRONTEND_SESSION_NAME) -d 'source .venv/bin/activate; cd frontend; pnpm run dev'

# Rebuild all, then stop, then start
rebuild-all-restart: backend-rebuild frontend-build stop start

# Stop both backend and frontend sessions
stop:
	tmux kill-session -t $(BACKEND_SESSION_NAME)
	tmux kill-session -t $(FRONTEND_SESSION_NAME)
	cd backend && docker compose down

# Attach to the backend session
attach-backend:
	tmux a -t $(BACKEND_SESSION_NAME)

# Attach to the frontend session
attach-frontend:
	tmux a -t $(FRONTEND_SESSION_NAME)

# Restart both backend and frontend
restart: stop start

# Backend-specific targets
backend-build:
	cd backend && docker compose build

backend-rebuild:
	cd backend && docker compose down && docker compose build && docker compose up -d

backend-migrate:
	cd backend && poetry run python init_db.py

backend-worker:
	cd backend && poetry run arq src.instorage.worker.worker.WorkerSettings

backend-logs:
	cd backend && docker compose logs -f

backend-test:
	cd backend && poetry run pytest

backend-lint:
	cd backend && poetry run pylint src

backend-fmt:
	cd backend && poetry run black src

# Frontend-specific targets (add your frontend commands here)
frontend-build:
	cd frontend && pnpm run build

frontend-test:
	cd frontend && pnpm run test

frontend-lint:
	cd frontend && pnpm run lint

# ... add more targets as needed ...
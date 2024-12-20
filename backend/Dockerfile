FROM python:3.12-slim-bullseye

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libmagic1 \
        ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /backend

# Copy source code
COPY . .
#COPY src ./src
#COPY init_db.py ./
#COPY alembic ./alembic
#COPY alembic.ini ./alembic.ini
#COPY .env ./.env
#COPY pyproject.toml poetry.lock ./

RUN pip install poetry

RUN poetry install

COPY entrypoint.sh ./
RUN chmod +x entrypoint.sh

CMD ["./entrypoint.sh"]

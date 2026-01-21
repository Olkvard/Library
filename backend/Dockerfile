FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

COPY app app

CMD ["sh", "-c", "\
until nc -z db 5432; do echo waiting for db; sleep 1; done; \
python -m app.db.init_db; \
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000"]
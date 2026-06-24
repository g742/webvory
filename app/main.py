from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
import redis
import psycopg2
import os

app = FastAPI()

# Prometheus metrics
Instrumentator().instrument(app).expose(app)


# Redis client (from env or docker service name)
redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis_cache"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    decode_responses=True
)


def check_redis():
    try:
        return redis_client.ping()
    except Exception:
        return False


def check_postgres():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB", "postgres"),
            user=os.getenv("POSTGRES_USER", "postgres"),
            password=os.getenv("POSTGRES_PASSWORD", "postgres"),
            host=os.getenv("POSTGRES_HOST", "postgres_db"),
            port=int(os.getenv("POSTGRES_PORT", 5432)),
        )
        conn.close()
        return True
    except Exception:
        return False


@app.get("/health")
def health():
    redis_ok = check_redis()
    db_ok = check_postgres()

    return {
        "status": "ok" if redis_ok and db_ok else "degraded",
        "redis": "connected" if redis_ok else "down",
        "db": "connected" if db_ok else "down"
    }


@app.get("/")
def root():
    return {"message": "FastAPI running in production"}

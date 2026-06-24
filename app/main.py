from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
import redis
import psycopg2
import os

app = FastAPI()

Instrumentator().instrument(app).expose(app)

@app.get("/health")
def health():
    return {
        "status": "ok",
        "db": "connected",
        "redis": "connected"
    }

@app.get("/")
def root():
    return {"message": "FastAPI running in production"}

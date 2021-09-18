# app.py
from functools import lru_cache
from typing import Dict

import uvicorn
from fastapi import FastAPI, Request

from config import settings, logging
from database.dynamodb import Table

logger = logging.getLogger(__name__)


app = FastAPI()


@app.get("/")
def home():
    return {"hello": "world", "say hi": settings.admin_email}


@app.get("/pairs/filter/")
def filter_pairs(
    correlation_type: str,
    bigger_than: str,
    smaller_than: str,
    order_by: str,
    limit: int,
):
    """
    Gets filtered correlations
    """
    # pairs/filter/?correlation_type=pearson&bigger_than=None&smaller_than=-0.8&order_by=DESC&limit=15

    correlations = Table(settings.DYNAMODB_TABLE)
    response = correlations.filter(
        correlation_type=correlation_type,
        bigger_than=bigger_than,
        smaller_than=smaller_than,
        order_by=order_by,
        limit=limit,
    )

    return response


if __name__ == "__main__":
    uvicorn.run(app)

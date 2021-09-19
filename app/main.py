# app.py
from functools import lru_cache
from typing import Dict

from fastapi import FastAPI
from mangum import Mangum

from app.config import settings, logging
from app.database.dynamodb import Table

logger = logging.getLogger(__name__)


app = FastAPI()


@app.get("/")
def home():
    return {"hello": "world", "say hi": settings.admin_email}


@app.get("/foo/bar/")
def filter_pairs(bb:int = 33, cc:str="abc"):
    print("Test trst")
    return {"foo": bb}


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

    print("This is for debugging 1")

    correlations = Table(settings.DYNAMODB_TABLE)
    print("This is for debugging 2")
    print(correlations)
    response = correlations.filter(
        correlation_type=correlation_type,
        bigger_than=bigger_than,
        smaller_than=smaller_than,
        order_by=order_by,
        limit=limit,
    )
    print("This is for debugging 3")

    return response


handler = Mangum(app=app)

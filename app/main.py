# app.py
from functools import lru_cache
from fastapi.params import Depends

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

from app.config import settings, logging
from app.database.dynamodb import Table

from .serializers import Filter, FilterResponse

logger = logging.getLogger(__name__)


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_WHITELIST,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"hello": "world", "say hi": settings.admin_email}


@app.get("/pairs/filter/", response_model=FilterResponse)
def filter_pairs(filter: Filter = Depends()):
    print(filter)
    """
    Gets filtered correlations
    """
    # pairs/filter/?correlation_type=pearson&bigger_than=None&smaller_than=-0.8&order_by=DESC&limit=15

    correlations = Table(settings.DYNAMODB_TABLE)
    response = correlations.filter(**filter.dict())

    return response


handler = Mangum(app=app)

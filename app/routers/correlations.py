from fastapi import Depends, APIRouter

from app.config import settings, logging
from app.database.dynamodb import Table
from app.serializers import Filter, FilterResponse


router = APIRouter(prefix="/correlations", tags=["Correlations"])


@router.get("", response_model=FilterResponse)
def filter_pairs(filter: Filter = Depends()):
    print(filter)
    """
    Gets filtered correlations
    """
    # correlations/?correlation_type=pearson&bigger_than=None&smaller_than=-0.8&order_by=DESC&limit=15

    correlations = Table(settings.DYNAMODB_TABLE)
    response = correlations.filter(**filter.dict())

    return response

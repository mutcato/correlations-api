from datetime import datetime
import decimal
from typing import Dict, List, Optional

from pydantic import BaseModel


class Filter(BaseModel):
    correlation_type: Optional[str] = "pearson"
    bigger_than: Optional[str]
    smaller_than: Optional[str]
    limit: Optional[int]
    contain: Optional[str]
    order_by: Optional[str] = "DESC"
    limit: int = 10
    date: str = str(datetime.today().date())


class FilterSingleResponse(BaseModel):
    """Serializes filter endpoint"""

    pair: str
    master: str
    slave: str
    pearson_corr: decimal.Decimal
    kendall_corr: decimal.Decimal
    spearman_corr: decimal.Decimal
    date: str
    interval: str


class FilterResponse(BaseModel):
    data: List[FilterSingleResponse]

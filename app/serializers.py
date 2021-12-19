from datetime import datetime
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
    """Serializes for filter endpoint"""

    pair: str
    master: str
    slave: str
    pearson_corr: str
    kendall_corr: str
    spearman_corr: str
    date: str
    interval: str
    

class FilterResponse(BaseModel):
    data: List[FilterSingleResponse]

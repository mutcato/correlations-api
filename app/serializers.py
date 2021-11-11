from datetime import datetime
from typing import Dict, Optional

from pydantic import BaseModel


class Filter(BaseModel):
    correlation_type: Optional[str] = "pearson"
    bigger_than: Optional[str]
    smaller_than: Optional[str]
    limit: Optional[int]
    contain: Optional[str]
    order_by: Optional[str] = "DESC"
    date: str = str(datetime.today().date())

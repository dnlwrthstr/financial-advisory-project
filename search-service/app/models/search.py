import strawberry
from typing import List, Optional
from datetime import datetime

@strawberry.type
class SearchResult:
    """
    Represents a search result item.
    """
    id: str
    title: str
    description: Optional[str] = None
    type: str
    score: float
    created_at: datetime
    updated_at: datetime
    url: Optional[str] = None
    metadata: Optional[dict] = None

@strawberry.input
class SearchFilter:
    """
    Input type for search filters.
    """
    field: str
    value: str
    operator: str = "eq"  # eq, ne, gt, lt, gte, lte, contains
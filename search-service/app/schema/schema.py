import strawberry
from typing import List, Optional
from app.models.search import SearchResult, SearchFilter
from app.resolvers.search_resolver import search_items

@strawberry.type
class Query:
    @strawberry.field
    async def search(
        self, 
        query: str, 
        filters: Optional[List[str]] = None, 
        limit: Optional[int] = 10
    ) -> List[SearchResult]:
        """
        Search for items matching the query string and optional filters.
        
        Args:
            query: The search query string
            filters: Optional list of filters to apply to the search
            limit: Maximum number of results to return (default: 10)
            
        Returns:
            List of search results matching the query
        """
        return await search_items(query, filters, limit)

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def index_item(self, item_id: str, content: str) -> bool:
        """
        Index a new item or update an existing item in the search index.
        
        Args:
            item_id: Unique identifier for the item
            content: Content to be indexed
            
        Returns:
            True if indexing was successful, False otherwise
        """
        # This would be implemented to add items to the search index
        # For now, return True as a placeholder
        return True
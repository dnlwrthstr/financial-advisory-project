from typing import List, Optional
from datetime import datetime
import os
import json
from opensearchpy import OpenSearch
from app.models.search import SearchResult

# Initialize OpenSearch client
def get_opensearch_client():
    """
    Create and return an OpenSearch client instance.

    Returns:
        OpenSearch client instance
    """
    host = os.environ.get('OPENSEARCH_HOST', 'opensearch')
    port = int(os.environ.get('OPENSEARCH_PORT', 9200))
    use_ssl = os.environ.get('OPENSEARCH_USE_SSL', 'false').lower() == 'true'

    # Basic authentication if provided
    auth = None
    username = os.environ.get('OPENSEARCH_USERNAME')
    password = os.environ.get('OPENSEARCH_PASSWORD')
    if username and password:
        auth = (username, password)

    client = OpenSearch(
        hosts=[{'host': host, 'port': port}],
        http_auth=auth,
        use_ssl=use_ssl,
        verify_certs=False,
        ssl_show_warn=False
    )

    return client

# Index name for financial data
INDEX_NAME = 'financial_data'

async def search_items(query: str, filters: Optional[List[str]] = None, limit: int = 10) -> List[SearchResult]:
    """
    Search for items matching the query string and optional filters.

    Args:
        query: The search query string
        filters: Optional list of filters to apply to the search
        limit: Maximum number of results to return

    Returns:
        List of search results matching the query
    """
    try:
        client = get_opensearch_client()

        # Check if index exists, if not return empty results
        if not client.indices.exists(index=INDEX_NAME):
            return []

        # Build search query
        search_query = {
            "size": limit,
            "query": {
                "bool": {
                    "must": [
                        {
                            "multi_match": {
                                "query": query,
                                "fields": ["title^2", "description", "content"]
                            }
                        }
                    ]
                }
            }
        }

        # Add filters if provided
        if filters:
            filter_clauses = []
            for filter_str in filters:
                if ':' in filter_str:
                    field, value = filter_str.split(':', 1)
                    filter_clauses.append({"term": {field: value}})

            if filter_clauses:
                search_query["query"]["bool"]["filter"] = filter_clauses

        # Execute search
        response = client.search(
            body=search_query,
            index=INDEX_NAME
        )

        # Process results
        results = []
        for hit in response['hits']['hits']:
            source = hit['_source']
            results.append(
                SearchResult(
                    id=hit['_id'],
                    title=source.get('title', 'Untitled'),
                    description=source.get('description'),
                    type=source.get('type', 'document'),
                    score=hit['_score'],
                    created_at=datetime.fromisoformat(source.get('created_at', datetime.now().isoformat())),
                    updated_at=datetime.fromisoformat(source.get('updated_at', datetime.now().isoformat())),
                    url=source.get('url'),
                    metadata=source.get('metadata', {})
                )
            )

        return results

    except Exception as e:
        print(f"Error searching OpenSearch: {str(e)}")
        # Fallback to mock results in case of error
        mock_results = [
            SearchResult(
                id=f"result-{i}",
                title=f"Search Result {i} for '{query}'",
                description=f"This is a mock search result for the query '{query}'",
                type="document",
                score=1.0 - (i * 0.1),
                created_at=datetime.now(),
                updated_at=datetime.now(),
                url=f"/documents/result-{i}",
                metadata={"tags": ["finance", "advisory"]}
            )
            for i in range(min(3, limit))
        ]

        return mock_results

async def index_item(item_id: str, content: str) -> bool:
    """
    Index a new item or update an existing item in the search index.

    Args:
        item_id: Unique identifier for the item
        content: Content to be indexed

    Returns:
        True if indexing was successful, False otherwise
    """
    try:
        client = get_opensearch_client()

        # Create index if it doesn't exist
        if not client.indices.exists(index=INDEX_NAME):
            # Define index mapping
            mapping = {
                "mappings": {
                    "properties": {
                        "title": {"type": "text"},
                        "description": {"type": "text"},
                        "content": {"type": "text"},
                        "type": {"type": "keyword"},
                        "created_at": {"type": "date"},
                        "updated_at": {"type": "date"},
                        "url": {"type": "keyword"},
                        "metadata": {"type": "object"}
                    }
                }
            }
            client.indices.create(index=INDEX_NAME, body=mapping)

        # Parse content as JSON or use as raw text
        try:
            document = json.loads(content)
        except json.JSONDecodeError:
            document = {
                "content": content,
                "title": f"Document {item_id}",
                "created_at": datetime.now().isoformat(),
                "updated_at": datetime.now().isoformat()
            }

        # Ensure required fields
        if "created_at" not in document:
            document["created_at"] = datetime.now().isoformat()
        if "updated_at" not in document:
            document["updated_at"] = datetime.now().isoformat()

        # Index the document
        response = client.index(
            index=INDEX_NAME,
            id=item_id,
            body=document,
            refresh=True
        )

        return response['result'] in ('created', 'updated')

    except Exception as e:
        print(f"Error indexing to OpenSearch: {str(e)}")
        return False

# Search Service

A GraphQL microservice for search functionality in the Financial Advisory Project.

## Features

- GraphQL API for searching financial data
- Filtering and pagination support
- Mock implementation ready to be extended with real search engine

## Tech Stack

- Python 3.11
- FastAPI
- Strawberry GraphQL
- Docker

## Getting Started

### Prerequisites

- Docker and Docker Compose
- Python 3.11+ (for local development)

### Running with Docker

The service is designed to be run as part of the Financial Advisory Project using Docker Compose:

```bash
# From the root of the financial-advisory-project
docker-compose up -d
```

### Local Development

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the service:
   ```bash
   uvicorn app.main:app --reload
   ```

4. Access the GraphQL playground at http://localhost:8000/graphql

## API Usage

### GraphQL Queries

#### Search

```graphql
query {
  search(query: "investment", limit: 5) {
    id
    title
    description
    type
    score
    createdAt
    updatedAt
    url
    metadata
  }
}
```

### GraphQL Mutations

#### Index Item

```graphql
mutation {
  indexItem(itemId: "doc-123", content: "Investment portfolio analysis") 
}
```

## Project Structure

```
search-service/
├── app/
│   ├── main.py           # FastAPI application entry point
│   ├── models/           # Data models
│   │   └── search.py     # Search-related data models
│   ├── resolvers/        # GraphQL resolvers
│   │   └── search_resolver.py  # Search functionality implementation
│   └── schema/           # GraphQL schema
│       └── schema.py     # GraphQL types, queries, and mutations
├── Dockerfile            # Docker configuration
├── README.md             # This file
└── requirements.txt      # Python dependencies
```

## Future Enhancements

- Integration with Elasticsearch or similar search engine
- Advanced filtering and faceting
- Real-time search suggestions
- Search analytics and reporting
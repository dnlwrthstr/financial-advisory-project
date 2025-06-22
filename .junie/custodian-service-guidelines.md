# Custodian Service Project Guidelines

## Project Overview
The Custodian Service is a FastAPI backend service that implements custodian interfaces as specified in OpenWealth standards. It uses MongoDB as the database and provides RESTful APIs for the frontend application.

### Purpose
The service provides:
- OpenWealth-compliant API endpoints for financial data
- Authentication and authorization
- Data validation and transformation
- Integration with external financial data providers
- Persistent storage of financial data

## Project Structure
The project follows a modular structure to support maintainability and scalability:

```
/app
  /api             # API routes and endpoints
    /v1            # API version 1
      /endpoints   # API endpoint modules
  /core            # Core application code
    /config        # Configuration management
    /security      # Authentication and authorization
  /db              # Database models and connections
    /models        # MongoDB models
    /repositories  # Data access layer
  /schemas         # Pydantic schemas for request/response validation
  /services        # Business logic services
  /utils           # Utility functions
/data              # Sample data and database initialization scripts
/tests             # Test files
main.py            # Application entry point
requirements.txt   # Python dependencies
Dockerfile         # Container configuration
```

## Development Guidelines

### Prerequisites
- Python 3.8+
- MongoDB
- Docker (for containerized development)
- Git

### Environment Setup
1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables:
   - Copy `.env.example` to `.env`
   - Update MongoDB connection string and other settings

### Testing
- Write tests using pytest
- Run tests with `pytest`
- Ensure all tests pass before submitting changes
- Use test coverage to identify untested code

### Code Style
- Follow PEP 8 guidelines
- Use type hints for all function parameters and return values
- Document all public functions and classes with docstrings
- Use async/await for I/O-bound operations

## API Documentation
- Document all API endpoints in API_DOCUMENTATION.md
- Include request/response examples
- Specify authentication requirements
- Note any rate limits or other constraints

## Error Handling
- Use appropriate HTTP status codes
- Return consistent error response structures
- Log errors with sufficient context for debugging
- Handle expected exceptions gracefully

## Security Considerations
- Implement proper authentication and authorization
- Validate all input data
- Sanitize data before storing or returning it
- Use HTTPS for all communications
- Follow OWASP security guidelines
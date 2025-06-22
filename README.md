# Financial Advisory Project

## Project Overview
This project is a comprehensive financial advisory application built with a microservices architecture. It consists of two main components:

1. **Custodian Service**: A FastAPI backend service that implements custodian interfaces as specified in OpenWealth standards, using MongoDB as the database.
2. **Frontend**: A modern, modular React + Vite frontend for the OpenWealth-based Custodian Service.

The components are organized as Git submodules, allowing developers to work on them independently while maintaining a cohesive application.

## Repository Structure
```
financial-advisory-project/
├── .git/                  # Git repository data
├── .gitmodules            # Submodule configuration
├── custodian-service/     # Backend service (submodule)
├── frontend/              # Frontend application (submodule)
└── docker-compose.yml     # Docker Compose configuration for the entire application
```

## Submodule Management

### Initializing Submodules
When you first clone this repository, you need to initialize and update the submodules:

```bash
# Clone the main repository
git clone <repository-url>
cd financial-advisory-project

# Initialize and update submodules
git submodule init
git submodule update
```

Alternatively, you can clone the repository with submodules in a single command:

```bash
git clone --recurse-submodules <repository-url>
```

### Updating Submodules
To update the submodules to their latest versions:

```bash
git submodule update --remote
```

### Working with Submodules

#### Making Changes to a Submodule
When you want to make changes to a submodule:

1. Navigate to the submodule directory:
   ```bash
   cd custodian-service  # or cd frontend
   ```

2. Ensure you're on the correct branch:
   ```bash
   git checkout main  # or another branch
   ```

3. Make your changes, commit them, and push to the submodule's remote repository:
   ```bash
   git add .
   git commit -m "Your commit message"
   git push origin main  # or another branch
   ```

4. Return to the main repository and update the submodule reference:
   ```bash
   cd ..
   git add custodian-service  # or frontend
   git commit -m "Update submodule reference"
   git push
   ```

#### Pulling Changes from Submodules
To pull the latest changes from the submodules:

```bash
git submodule update --remote --merge
```

## Development Workflow

### Working on the Custodian Service

#### Prerequisites
- Python 3.8+
- MongoDB

#### Setup and Development
1. Navigate to the custodian-service directory:
   ```bash
   cd custodian-service
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   - Copy the `.env.example` file to `.env`
   - Update the MongoDB connection URL and other settings as needed

5. Start the development server:
   ```bash
   uvicorn main:app --reload
   ```

6. The API will be available at http://localhost:8000.

#### Running Tests
To run tests for the custodian service:

```bash
cd custodian-service
pytest
```

### Working on the Frontend

#### Prerequisites
- Node.js (v18 or later)
- npm or pnpm

#### Setup and Development
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

4. The application will be available at http://localhost:3003.

#### Running Tests
To run tests for the frontend:

```bash
cd frontend
npm run test
```

## Docker Setup

### Running the Entire Application
You can run the entire application using Docker Compose:

```bash
docker-compose up -d
```

This will start the following services:
- MongoDB on port 27017
- Custodian Service on port 8010
- Frontend on port 3002

### Running Individual Components
You can also run individual components using Docker:

#### Custodian Service
```bash
cd custodian-service
docker-compose up -d
```

#### Frontend
```bash
cd frontend
docker build -t custodian-frontend .
docker run -p 3002:3002 custodian-frontend
```

## API Documentation
Once the custodian service is running, you can access the interactive API documentation at:
- Swagger UI: http://localhost:8010/docs
- ReDoc: http://localhost:8010/redoc

## License
MIT
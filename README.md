# Financial Advisory Project

## Project Overview
The Financial Advisory Project is a comprehensive financial advisory application built with a microservices architecture. It consists of two main components:

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
├── search-service/        # Search service
├── k8s/                   # Kubernetes manifests
└── docker-compose.yml     # Docker Compose configuration for the entire application
```

## Submodule Handling

### Working with Submodules
This project uses Git submodules to manage the custodian-service and frontend components. When working with submodules:

1. **Cloning the Repository**:
   ```bash
   git clone --recurse-submodules <repository-url>
   ```
   Or if already cloned:
   ```bash
   git submodule init
   git submodule update
   ```

2. **Updating Submodules**:
   ```bash
   git submodule update --remote --merge
   ```

3. **Making Changes to a Submodule**:
   - Navigate to the submodule directory
   - Make changes, commit, and push to the submodule's repository
   - Return to the main repository and update the submodule reference

4. **Adding a New Submodule**:
   ```bash
   git submodule add <repository-url> <path>
   git commit -m "Add new submodule"
   git push
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
- OpenSearch on ports 9200 and 9600
- Zookeeper on port 2181
- Kafka on ports 9092 (internal) and 29092 (external)
- Kafka UI on port 8080
- Custodian Service on port 8010
- Search Service on port 8020
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

## Kafka Integration

### Overview
This project uses Apache Kafka for event streaming and message processing. Kafka enables reliable, scalable, and fault-tolerant communication between microservices.

### Components
- **Zookeeper**: Manages the Kafka cluster state
- **Kafka Broker**: The message broker that handles publishing and subscribing to message streams
- **Kafka UI**: A web interface for managing and monitoring Kafka

### Accessing Kafka
- Kafka Broker is accessible internally at `kafka:9092` and externally at `localhost:29092`
- Kafka UI is available at http://localhost:8080

### Working with Kafka

#### Creating Topics
You can create topics using the Kafka UI or with the Kafka CLI tools:

```bash
docker exec -it kafka kafka-topics --create --topic my-topic --bootstrap-server kafka:9092 --partitions 1 --replication-factor 1
```

#### Producing Messages
To produce messages to a Kafka topic:

```bash
docker exec -it kafka kafka-console-producer --topic my-topic --bootstrap-server kafka:9092
```

#### Consuming Messages
To consume messages from a Kafka topic:

```bash
docker exec -it kafka kafka-console-consumer --topic my-topic --bootstrap-server kafka:9092 --from-beginning
```

#### Using Kafka in Services
Services can connect to Kafka using the following connection string:
- From inside Docker network: `kafka:9092`
- From host machine: `localhost:29092`

## API Documentation
Once the custodian service is running, you can access the interactive API documentation at:
- Swagger UI: http://localhost:8010/docs
- ReDoc: http://localhost:8010/redoc

## Integrating New Services

When integrating a new service into the project:

1. **Create a New Repository** for the service following the project's coding standards
2. **Add as a Submodule** to the main repository
3. **Update docker-compose.yml** to include the new service
4. **Configure Service Communication**:
   - Use environment variables for service discovery
   - Implement proper error handling for inter-service communication
   - Document API endpoints in an API_DOCUMENTATION.md file

5. **Service Requirements**:
   - Include a Dockerfile for containerization
   - Provide a README.md with setup instructions
   - Include tests for critical functionality
   - Follow the project's error handling and logging standards

## Integrating New Frontend Functionality

When adding new frontend features:

1. **Follow the Existing Structure**:
   ```
   frontend/src/
   ├── api/            # API clients and endpoints
   ├── components/     # Reusable UI components
   ├── routes/         # Page components
   └── App.tsx         # Main application component
   ```

2. **Component Organization**:
   - Create domain-specific directories for new features
   - Keep components small and focused on a single responsibility
   - Use React hooks for state management and side effects

3. **API Integration**:
   - Add new API clients in the `api/` directory
   - Use consistent error handling and loading states
   - Document API usage in component comments

4. **Testing**:
   - Write tests for new components and functionality
   - Run existing tests to ensure no regressions

## Enabling Micro Frontend Development

To support future micro frontend development:

1. **Module Federation**:
   - Update the Vite configuration to support Webpack Module Federation
   - Define clear boundaries between micro frontends
   - Create a shell application that loads micro frontends

2. **Shared Dependencies**:
   - Maintain a list of shared dependencies across micro frontends
   - Use a consistent versioning strategy for shared libraries

3. **Routing**:
   - Implement a routing strategy that supports micro frontends
   - Consider using single-spa or similar framework for micro frontend orchestration

4. **Communication**:
   - Define clear interfaces for communication between micro frontends
   - Use events or a shared state management solution for cross-micro frontend communication

## Kubernetes Deployment

For local and production Kubernetes deployment:

1. **Local Development with Docker Desktop K8s**:
   - Enable Kubernetes in Docker Desktop
   - Use `kubectl apply -f k8s/` to deploy locally
   - Create a development namespace: `kubectl create namespace financial-advisory-dev`

2. **Kubernetes Configuration**:
   - Store Kubernetes manifests in a `k8s/` directory
   - Create separate manifests for each component:
     - Deployments
     - Services
     - ConfigMaps
     - Secrets (use .gitignore for sensitive data)
     - Ingress rules

3. **Resource Requirements**:
   - Define resource limits and requests for all containers
   - Configure horizontal pod autoscaling for production

4. **Monitoring and Logging**:
   - Implement health checks for all services
   - Configure liveness and readiness probes
   - Set up centralized logging with ELK or similar stack

## Component Versioning and Registry

For versioning and publishing components:

1. **Versioning Strategy**:
   - Use Semantic Versioning (SemVer) for all components
   - Tag releases in Git repositories
   - Document breaking changes in CHANGELOG.md files

2. **Container Registry**:
   - Push container images to a private registry (e.g., Docker Hub, AWS ECR, GitHub Container Registry)
   - Tag images with both version and `latest` tags
   - Implement CI/CD pipelines for automated builds and pushes

3. **Frontend Component Registry**:
   - For shared UI components, use a package registry (npm, GitHub Packages)
   - Publish components with proper versioning
   - Document component usage and props

4. **Continuous Integration**:
   - Run tests before publishing new versions
   - Generate and publish documentation automatically
   - Enforce code quality standards through linting and code reviews

## License
MIT

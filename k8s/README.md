# Kubernetes Deployment for Financial Advisory Project

This directory contains Kubernetes manifests for deploying the Financial Advisory Project in a Kubernetes cluster.

## Directory Structure

```
k8s/
├── README.md                     # This file
├── namespace.yaml                # Namespace definition
├── mongo/                        # MongoDB deployment
│   ├── deployment.yaml           # MongoDB deployment
│   ├── service.yaml              # MongoDB service
│   └── persistent-volume.yaml    # Persistent volume for MongoDB data
├── custodian-service/            # Custodian Service deployment
│   ├── deployment.yaml           # Custodian Service deployment
│   ├── service.yaml              # Custodian Service service
│   └── configmap.yaml            # ConfigMap for Custodian Service
├── frontend/                     # Frontend deployment
│   ├── deployment.yaml           # Frontend deployment
│   ├── service.yaml              # Frontend service
│   └── configmap.yaml            # ConfigMap for Frontend
└── ingress.yaml                  # Ingress for external access
```

## Getting Started

### Prerequisites

- Kubernetes cluster (local or remote)
- kubectl installed and configured
- Docker images for custodian-service and frontend

### Deployment

1. Create the namespace:
   ```bash
   kubectl apply -f namespace.yaml
   ```

2. Deploy MongoDB:
   ```bash
   kubectl apply -f mongo/
   ```

3. Deploy Custodian Service:
   ```bash
   kubectl apply -f custodian-service/
   ```

4. Deploy Frontend:
   ```bash
   kubectl apply -f frontend/
   ```

5. Deploy Ingress:
   ```bash
   kubectl apply -f ingress.yaml
   ```

### Accessing the Application

Once deployed, the application can be accessed through the Ingress at:
- Frontend: http://financial-advisory.local
- API: http://financial-advisory.local/api

For local development with Docker Desktop Kubernetes, add the following entry to your hosts file:
```
127.0.0.1 financial-advisory.local
```

## Configuration

### Environment Variables

Environment variables are defined in the ConfigMap files for each service. Update these files to change the configuration.

### Secrets

Sensitive information should be stored in Kubernetes Secrets. Create a Secret for database credentials:

```bash
kubectl create secret generic db-credentials \
  --namespace=financial-advisory \
  --from-literal=username=admin \
  --from-literal=password=secure-password
```

## Scaling

The deployments can be scaled horizontally:

```bash
kubectl scale deployment custodian-service --replicas=3 -n financial-advisory
```

## Monitoring

Set up monitoring using Prometheus and Grafana:

1. Install Prometheus Operator:
   ```bash
   kubectl apply -f https://github.com/prometheus-operator/prometheus-operator/releases/download/v0.59.1/bundle.yaml
   ```

2. Create ServiceMonitor resources for each service.

## Troubleshooting

### Checking Logs

```bash
kubectl logs -f deployment/custodian-service -n financial-advisory
kubectl logs -f deployment/frontend -n financial-advisory
```

### Checking Pod Status

```bash
kubectl get pods -n financial-advisory
kubectl describe pod <pod-name> -n financial-advisory
```
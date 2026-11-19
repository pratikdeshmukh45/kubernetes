# Day 4 – OpsPulse Service Health API on Kubernetes

## Project Overview

OpsPulse is a Python Flask-based service health API built from scratch and deployed on Kubernetes using Docker.

The project demonstrates application development, containerization, Kubernetes Deployments, Services, health probes and resource management.

## Architecture

- Python Flask REST API
- Gunicorn WSGI server
- Docker container
- Kubernetes Deployment with 2 replicas
- Kubernetes ClusterIP Service
- Liveness and readiness probes
- CPU and memory requests and limits

## API Endpoints

| Endpoint | Description |
|---|---|
| `/` | Application information |
| `/health` | Application health |
| `/api/services` | Returns monitored services |

## Deployment

The application was containerized using Docker and deployed to a local Minikube Kubernetes cluster.

The Kubernetes Deployment maintains two replicas.

The ClusterIP Service exposes port 80 and forwards traffic to container port 5000.

## Failure Testing

An invalid container image was configured intentionally to observe image-related Pod failures.

The issue was investigated using `kubectl describe pod` and Kubernetes Events.

The original image was restored and the Deployment returned to a healthy state.

## Commands Used

- `docker build`
- `minikube image build`
- `kubectl apply`
- `kubectl get pods`
- `kubectl get deployments`
- `kubectl get services`
- `kubectl describe pod`
- `kubectl logs`
- `kubectl rollout status`
- `kubectl port-forward`

## Screenshots

Add screenshots of the successful deployment, Pods, Service, API responses and failure investigation.

## Key Learnings

- Building a REST API using Flask
- Understanding Docker image construction
- Deploying custom container images on Minikube
- Understanding Kubernetes Deployments and Services
- Configuring readiness and liveness probes
- Understanding resource requests and limits
- Troubleshooting image-related Pod failures

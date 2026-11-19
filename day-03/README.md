
# Day 3 - Kubernetes Services and Networking

## Objective
Understand Kubernetes Services and expose NGINX Pods
using ClusterIP, NodePort and LoadBalancer.

## Concepts Covered
1. Kubernetes Services
2. ClusterIP
3. NodePort
4. LoadBalancer
5. Service selectors
6. Endpoints and EndpointSlices
7. Kubernetes DNS and CoreDNS
8. Service troubleshooting

## Practical Tasks
- Created NGINX Deployment with 3 replicas.
- Created ClusterIP Service.
- Tested Service using port-forward.
- Inspected Service endpoints.
- Deleted a Pod and observed self-healing.
- Created NodePort Service.
- Tested external access.
- Created LoadBalancer Service.
- Tested Kubernetes DNS.

## Important Commands

kubectl get svc
kubectl describe svc nginx-clusterip
kubectl get endpoints
kubectl get endpointslices
kubectl get pods --show-labels
kubectl port-forward svc/nginx-clusterip 8080:80
minikube service nginx-nodeport

## Learning Outcome
Understood how Kubernetes Services provide stable
network access to dynamically changing Pods.

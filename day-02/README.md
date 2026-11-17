
# Kubernetes Day 2 - ReplicaSets, Scaling and Rolling Updates

## Objective
Understand how Deployments manage ReplicaSets and Pods.

## Topics Covered
1. ReplicaSets and desired state
2. Self-healing
3. Scaling up and down
4. Rolling updates
5. Rollbacks
6. Deployment revisions
7. Failed image deployment troubleshooting

## Commands Practised

### Check resources
kubectl get deployments
kubectl get replicasets
kubectl get pods -o wide

### Scaling
kubectl scale deployment nginx-day2 --replicas=5
kubectl scale deployment nginx-day2 --replicas=2

### Rolling updates
kubectl set image deployment/nginx-day2 nginx=nginx:1.28
kubectl rollout status deployment/nginx-day2

### Rollback
kubectl rollout history deployment/nginx-day2
kubectl rollout undo deployment/nginx-day2

## Key Learnings
- Deployment manages ReplicaSets.
- ReplicaSets maintain the desired Pod count.
- Kubernetes replaces deleted Pods.
- Rolling updates gradually replace old Pods.
- Rollbacks restore an earlier Deployment revision.
- ImagePullBackOff indicates an image retrieval problem.

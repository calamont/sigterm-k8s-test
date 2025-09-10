# README
A quick test to verify `SIGTERM` handling for a deployed Python app.

## Requirements
- Docker
- Minikube
- kubectl/kubectx (probably have these if you've set up the kraken CLI).

## How to run it

```bash
# Set up environment
minikube start
kubectx
# ^ Select minikube context

# Allow minikube to pull locally built docker images
eval $(minikube docker-env)

# Build and deploy
docker build -t sigtermtest .
kubectl apply -f deployment.yaml

# See results
kubectl delete -f deployment.yaml
kubectl get pods
# ^ Get pod name
kubectl logs <podname>
```

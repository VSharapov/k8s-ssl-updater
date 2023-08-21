#!/bin/bash

# Apply the namespace
kubectl apply -f namespace.yaml

# Apply the deployment within the namespace
kubectl apply -f deployment.yaml -n k8s-ssl-updater

echo "Deployment has been applied to the k8s-ssl-updater namespace."

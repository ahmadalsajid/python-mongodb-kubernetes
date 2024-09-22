# python-mongodb-kubernetes

Simple Python FastAPI app with MongoDB, orchestrated with Kubernetes

## Motivation

We will build a simple CRUD application with Python & FastAPI, and MongoDB as 
the database. All of them will be deployed to local kubernetes environment
(minikube). We will manage the `environment variables` and `secrets` with 
`ConfigMap` and `Secrets`. The python application will be a stateless 
application, whereas MongoDB will be stateful application to have persistent 
data. After that, we will introduce HPA for our application and put it through
rigorous stress test. Then, we will implement Nginx ingress and protect it from 
DDoS attack. Also, We will use Prometheus and Grafana to monitor our infra and
the applications.

## Installation

Before starting, we need to install 
 - [Docker Desktop](https://www.docker.com/products/docker-desktop/)
 - [minikube](https://minikube.sigs.k8s.io/docs/start/)
 - [kubectl](https://kubernetes.io/docs/tasks/tools/)

Now, start minikube
```
$ minikube start
😄  minikube v1.34.0 on Ubuntu 22.04 (amd64)
✨  Automatically selected the docker driver
📌  Using Docker driver with root privileges
❗  For an improved experience it's recommended to use Docker Engine instead of Docker Desktop.
Docker Engine installation instructions: https://docs.docker.com/engine/install/#server
👍  Starting "minikube" primary control-plane node in "minikube" cluster
🚜  Pulling base image v0.0.45 ...
💾  Downloading Kubernetes v1.31.0 preload ...
    > preloaded-images-k8s-v18-v1...:  326.69 MiB / 326.69 MiB  100.00% 402.36 
    > gcr.io/k8s-minikube/kicbase...:  487.90 MiB / 487.90 MiB  100.00% 356.55 
🔥  Creating docker container (CPUs=4, Memory=4096MB) ...
🐳  Preparing Kubernetes v1.31.0 on Docker 27.2.0 ...
    ▪ Generating certificates and keys ...
    ▪ Booting up control plane ...
    ▪ Configuring RBAC rules ...
🔗  Configuring bridge CNI (Container Networking Interface) ...
🔎  Verifying Kubernetes components...
    ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
🌟  Enabled addons: storage-provisioner, default-storageclass
🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default

```

## Tasks

| **Task ID** | **Details**                                               | **Status**         | **Comment(s)** |
|-------------|-----------------------------------------------------------|--------------------|----------------|
| Task-1      | Create dev environment with minikube                      | :white_check_mark: |                |
| Task-2      | ConfigMap and Secrets                                     | :x:                |                |
| Task-3      | Deploy Stateful Application (MongoDB)                     | :x:                |                |
| Task-4      | Deploy Stateless application, local image for FastAPI app | :x:                |                |
| Task-5      | HPA (Horizontal Pod Autoscaling)                          | :x:                |                |
| Task-6      | Nginx Ingress                                             | :x:                |                |
| Task-7      | DDoS protection                                           | :x:                |                |
| Task-8      | Prometheus Grafana integration for monitoring             | :x:                |                |
| Task-9      | To be amended in the future                               | :x:                |                |

## References
